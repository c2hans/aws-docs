---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/python.html
---

# Python in AL2027
<a name="python"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 With AL2027, you can use Python 3.14 at `/usr/bin/python3`. This is the system Python for AL2027. Python versions 3.9, 3.10, 3.11, 3.12, and 3.13 from AL2023 are not available in AL2027 at this time.

 The system Python remains Python 3.14 for the life of AL2027. Later Python versions are provided in separate, name-spaced packages, the same way they are in AL2023.

**Note**
 Do not change what the `/usr/bin/python3` symlink points to. Changing it might break core AL2027 functionality.

## Migrating to Python 3.14
<a name="python-migration"></a>

 If you are moving an application from AL2023 that targets an earlier Python version, for more information about upgrading, see the [Python 3.14 release notes](https://docs.python.org/3/whatsnew/3.14.html) on the Python documentation website.

## Python modules in AL2027
<a name="python-modules"></a>

 With AL2027, you can install commonly used Python libraries as RPMs using `dnf`, without building from source. These RPMs target the system version of Python. To find available modules, run:

```
dnf search python3
```

## Package Installation Security
<a name="python-security"></a>

 AL2027 turns on a *dependency cooldown* for *pip* by default. The configuration in `/etc/pip.conf` sets `uploaded-prior-to = P1D`, so *pip* skips the package versions that were published less than one day ago.

 To override the cooldown for a single command, use `--uploaded-prior-to=P0D`:

```
pip install --uploaded-prior-to=P0D {{package}}
```

 To change the cooldown setting, edit `/etc/pip.conf`. For more information, see [Secure your npm and pip package updates in Amazon Linux](https://aws.amazon.com/blogs/security/secure-your-npm-and-pip-package-updates-in-amazon-linux/) on the AWS Security Blog.
