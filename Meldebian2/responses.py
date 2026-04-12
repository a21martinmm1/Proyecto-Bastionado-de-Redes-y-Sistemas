cmd_responses = {
'ls': 'acct\nbt_firmware\nbugreports\ncache\ncharger\nconfig\nd\ndata\ndev\ndsp\netc\nfirmware\nmnt\nnonplat_file_contexts\nnonplat_property_contexts\nnonplat_seapp_contexts\noem\npersist\nplat_file_contexts\nplat_property_contexts\nplat_seapp_contexts\nplat_service_contexts\nproc\nres\nroot\nsbin\nsdcard\nsepolicy\nstorage\nsys\nsystem\ntombstones\nvendor\nls: ./vndservice_contexts: Permission denied\nls: ./ueventd.rc: Permission denied\nls: ./plat_hwservice_contexts: Permission denied\nls: ./nonplat_service_contexts: Permission denied\nls: ./nonplat_hwservice_contexts: Permission denied\nls: ./init.zygote64_32.rc: Permission denied\nls: ./init.zygote32.rc: Permission denied\nls: ./init.usb.rc: Permission denied\nls: ./init.usb.configfs.rc: Permission denied\nls: ./init.rc: Permission denied\nls: ./init.environ.rc: Permission denied\nls: ./init: Permission denied\nls: ./default.prop: Permission denied\n',
'getprop ro.product.model': 'SM-J700F',
'getprop ro.build.version.release': '8.1.0',
'getprop ro.product.manufacturer': 'samsung',
'getprop ro.product.brand': 'samsung',
'getprop ro.build.fingerprint': 'samsung/j7velte/j7veltedd:8.1.0/M1AJQ/J700FXXU3BSA1:user/release-keys',
'getprop ro.serialno': 'R58M93FZXXX',
'getprop': '''[ro.product.model]: [SM-J700F]
[ro.build.version.release]: [8.1.0]
[ro.product.manufacturer]: [samsung]
[ro.product.brand]: [samsung]
[ro.build.fingerprint]: [samsung/j7velte/j7veltedd:8.1.0/M1AJQ/J700FXXU3BSA1:user/release-keys]
[ro.serialno]: [R58M93FZXXX]
[net.hostname]: [android-3f2a1bc9]''',
'id': 'uid=2000(shell) gid=2000(shell) groups=2000(shell),1004(input),1007(log),1011(adb),1015(sdcard_rw),1028(sdcard_r),3001(net_bt_admin),3002(net_bt),3003(inet),3006(net_bw_stats) context=u:r:shell:s0',
'whoami': 'shell',
'uname': 'Linux',
'uname -a': 'Linux localhost 3.18.71-perf+ #1 SMP PREEMPT Wed Aug 15 12:04:01 KST 2018 armv7l',
'pwd': '/',
'echo hi': 'hi',
'echo $PATH': '/sbin:/vendor/bin:/system/sbin:/system/bin:/system/xbin',
'ls /data': 'opendir failed, Permission denied',
'ls /sdcard': '''Alarms
Android
DCIM
Download
Movies
Music
Notifications
Pictures
Podcasts
Ringtones''',
'ls /proc': '''1
acpi
buddyinfo
bus
cgroups
cmdline
cpuinfo
crypto
devices
diskstats
execdomains
fb
filesystems
fs
interrupts
iomem
ioports
irq
kallsyms
kcore
keys
kmsg
kpagecount
kpageflags
loadavg
locks
meminfo
misc
modules
mounts
net
pagetypeinfo
partitions
schedstat
slabinfo
softirqs
stat
swaps
timer_list
tty
uptime
version
vmallocinfo
vmstat
zoneinfo''',
'cat /proc/cpuinfo': '''Processor       : ARMv7 Processor rev 4 (v7l)
processor       : 0
BogoMIPS        : 38.40

processor       : 1
BogoMIPS        : 38.40

processor       : 2
BogoMIPS        : 38.40

processor       : 3
BogoMIPS        : 38.40

Hardware        : Qualcomm Technologies, Inc MSM8916
Revision        : 0000
Serial          : 0000000000000000''',
'cat /proc/meminfo': '''MemTotal:        1872160 kB
MemFree:          142312 kB
Buffers:           18432 kB
Cached:           612480 kB
SwapTotal:        524284 kB
SwapFree:         524284 kB''',
'cat /proc/version': 'Linux version 3.18.71-perf+ (dpi@SWDP2049) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Wed Aug 15 12:04:01 KST 2018',
'uptime': ' 14:32:05 up 3 days, 21:17,  0 users,  load average: 0.12, 0.08, 0.05',
'df': '''Filesystem           1K-blocks    Used Available Use% Mounted on
tmpfs                   936080     476   935604   1% /dev
tmpfs                   936080       0   936080   0% /mnt
/dev/block/mmcblk0p23  2359296 1873920   485376  80% /system
/dev/block/mmcblk0p28 12976128 2408448 10567680  19% /data
/dev/block/mmcblk0p25  1048576  188416   860160  18% /cache''',
'ifconfig': '''wlan0     Link encap:UNSPEC
          inet addr:192.168.1.105  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::a2e3:f1c2:3d4b:5e6f/64 Scope: Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:84231 errors:0 dropped:0 overruns:0 frame:0
          TX packets:62341 errors:0 dropped:0 overruns:0 carrier:0

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1''',
'netstat': '''Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 192.168.1.105:5555      0.0.0.0:*               LISTEN''',
'ip route': '''default via 192.168.1.1 dev wlan0 proto dhcp
192.168.1.0/24 dev wlan0 proto kernel scope link src 192.168.1.105''',
'ps': '''USER      PID  PPID  VSIZE   RSS   WCHAN    PC         NAME
root        1     0    2936  1352  SyS_epoll /init
root        2     0       0     0  kthreadd  kthreadd
shell    3241  3238    7316  1780  wait      /system/bin/sh
shell    3242  3241    3980   780  0         ps''',
'top -n 1': '''Tasks: 87 total,   1 running,  86 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.1 us,  0.8 sy,  0.0 ni, 97.1 id
KiB Mem:  1872160 total,   142312 free,  1112364 used
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
    1 root      20   0    2936   1352    980 S   0.0  0.1   0:02.14 init
  342 system    20   0  125648  28316   5480 S   1.2  1.5   2:31.08 system_server''',
'wget': 'wget: missing URL',
'curl': 'curl: try \'curl --help\' or \'curl --manual\' for more information',
'chmod': '',
'cd /': '',
'cd /tmp': '',
'cd /data/local/tmp': '',
}
