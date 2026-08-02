---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/python2.7-no-more.html
---

# Python 2.7 has been replaced with Python 3
<a name="python2.7-no-more"></a>

 AL2 provides support and security patches for Python 2.7 until June 2025, as part of our long-term support (LTS) commitment for AL2 core packages. This support extends beyond the upstream Python community declaration of Python 2.7 end-of-life of January 2020.

 AL2 uses the `yum` package manager, which has a hard dependency on Python 2.7. In AL2023 the `dnf` package manager has migrated to Python 3, and no longer requires Python 2.7. AL2023 has completely moved to Python 3.

**Note**
 AL2023 removed Python 2.7, so any OS components requiring Python are written to work with Python 3. To continue to use a version of Python provided by and supported by Amazon Linux, convert Python 2 code to Python 3.

For more information on Python on Amazon Linux, see [Python in AL2023](python.md).
