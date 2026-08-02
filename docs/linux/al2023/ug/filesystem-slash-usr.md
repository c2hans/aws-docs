---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-usr.html
---

# `/usr` (System Resources)
<a name="filesystem-slash-usr"></a>

 The `/usr` hierarchy is for vendor supplied Operating System resources. Except for the [`/usr/local`](#filesystem-slash-usr-local) hierarchy, nothing should modify anything under `/usr` except the OS package manager.

 Software applications must assume that `/usr` can be read-only. The `/usr` hierarchy must not be used for volitile data. Except for [`/usr/local`](#filesystem-slash-usr-local), the `/usr` hierarchy must not be used for any data that is added or changed outside of package installation/removal as done by the OS package manager. The OS package manager may assume that all of the `/usr` hierarchy (except [`/usr/local`](#filesystem-slash-usr-local)) is the same mountpoint.

 Software being installed outside of the OS package manager should not store data in `/usr` as this may impede any future invocation of the OS package manager. The [`/usr/local`](#filesystem-slash-usr-local) hierarchy is the exception, and is reserved for software outside of the OS package manager.

## `/usr/bin` (Executables)
<a name="filesystem-slash-usr-bin"></a>

 Executable files which should appear in the standard search `$PATH`, and are useful to invoke from a shell. Daemons and executables which are not useful to invoke from a shell instead live in `/usr/lib` or `/usr/libexec`.

## `/usr/include` (C/C\+\+ Headers)
<a name="filesystem-slash-usr-include"></a>

 The `/usr/include` directory contains C and C\+\+ header files, usually contained in packages with the `-devel` suffix.

## `/usr/lib` and `/usr/lib64` (Shared libraries)
<a name="filesystem-slash-usr-lib"></a>

 On Amazon Linux 2023, the `/usr/lib64` path is used for 64-bit shared libraries, and package data which is architecture dependent. Since AL2023 does not ship with any 32-bit userspace support, there are only 64-bit shared libraries available.

 The `/usr/lib` path is for static data from OS packages which is compatible with all architectures. This may include executables not usually invoked from a shell, which may also be found in `/usr/libexec`. Shared libraries are found in `/usr/lib64` rather than `/usr/lib`.

## `/usr/local` (System administrator installed software)
<a name="filesystem-slash-usr-local"></a>

 On Amazon Linux 2023, the `/usr/local` path is available for the system administrator to install software in, software that is not owned by the OS, and will not be touched by the OS. The default `/usr/local` hierarchy mirrors the `/` hierarchy.

## `/usr/share` (Shared resources)
<a name="filesystem-slash-usr-share"></a>

 Shared resources such as documentation, fonts, and time zone data live in `/usr/share`. It is common for various specifications to dictate exactly where and in what format data is stored in this directory.

### `/usr/share/doc` (Documentation)
<a name="filesystem-slash-usr-share-doc"></a>

 Documentation that comes with packages will be stored in `/usr/share/doc`.
