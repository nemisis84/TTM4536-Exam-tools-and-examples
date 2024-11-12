# Binwalk

Scanning Firmware:
- The primary - and by far the most popular - feature of binwalk is its signature scanning
- Binwalk can scan a firmware image for many different embedded file types and file systems
- Good for finding hidden files within files

Just give it a list of files to scan:
```
binwalk <filename>
```

You can tell binwalk to extract any files that it finds in the
firmware image with the -e option:
```
binwalk -e <filename>
```

binwalk can recursively scan files as it extracts them if you
also specify the -M option:

```
binwalk -Me <filename>
```

if the -r option is specified, any file signatures that couldn't
be extracted - or that resulted in 0-size files - will be
automatically deleted:
```
binwalk -Mre <filename>
```

To extract one specific signature type, specify one or more
-D type options:
```
binwalk -D 'png image:png' firmware.bin
```