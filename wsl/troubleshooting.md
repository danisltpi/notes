# Troubleshooting

## When Lxssmanager is stuck

First get the PID of svchost.exe running LxssManager, open the cmd as administrator and run:

`tasklist /svc /fi "imagename eq svchost.exe" | findstr LxssManager`
Grab the returned PID, then run task manager as administrator, in the details tab, search for the svchost.exe containing the PID, right click it and select 'end process tree'.

Now you should be able to restart wsl normally with 'wsl shutdown and wsl.

