---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-usr.html
---

# `/usr` (system resources)
<a name="filesystem-slash-usr"></a>

The `/usr` hierarchy is for vendor-supplied operating system resources. Except for the [`/usr/local`](#filesystem-slash-usr-local) hierarchy, nothing should modify anything under `/usr` except the OS package manager.

Software must assume that `/usr` can be read-only, and must not use it for volatile data. Software installed outside of the OS package manager belongs in [`/usr/local`](#filesystem-slash-usr-local), not elsewhere in `/usr`, so that it cannot interfere with package operations.

## Unified `/usr/bin` and `/usr/sbin`
<a name="filesystem-bin-sbin-merge"></a>

In AL2027, `/usr/sbin` is a symbolic link to `/usr/bin`. The executables that AL2023 shipped in `/usr/sbin`, such as `useradd`, `sysctl`, and `ip`, now live in `/usr/bin`. This follows the same change in [Unify bin and sbin](https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin) on the Fedora Project wiki.

Existing paths keep working: because `/sbin` and `/usr/sbin` both resolve to `/usr/bin`, a script that calls, for example, `/usr/sbin/ip` or `/sbin/ldconfig` runs unchanged. Commands formerly restricted to administrator search paths now also appear in every user's `$PATH`; the commands themselves still require the same privileges to do their work.

## `/usr/bin` (executables)
<a name="filesystem-slash-usr-bin"></a>

Executable files that appear in the standard search `$PATH` and are useful to invoke from a shell. Daemons and executables not useful from a shell live in `/usr/lib` or `/usr/libexec`.

## `/usr/include` (C/C\+\+ headers)
<a name="filesystem-slash-usr-include"></a>

C and C\+\+ header files, usually installed by packages with the `-devel` suffix.

## `/usr/lib` and `/usr/lib64` (shared libraries)
<a name="filesystem-slash-usr-lib"></a>

The `/usr/lib64` path holds 64-bit shared libraries and architecture-dependent package data. AL2027 does not ship 32-bit (i686) packages, so all shared libraries are 64-bit. The `/usr/lib` path is for static, architecture-independent package data, and might include executables not usually invoked from a shell, which might also be found in `/usr/libexec`.

## `/usr/local` (administrator-installed software)
<a name="filesystem-slash-usr-local"></a>

The `/usr/local` hierarchy is reserved for the system administrator to install software that is not owned by the OS. The OS does not touch it. Its layout mirrors the `/` hierarchy.

## `/usr/share` (shared resources)
<a name="filesystem-slash-usr-share"></a>

Architecture-independent shared resources such as documentation, fonts, and time zone data. Package documentation is installed under `/usr/share/doc`.
