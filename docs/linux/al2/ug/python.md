---
source_url: https://docs.aws.amazon.com/linux/al2/ug/python.html
---

# Python in AL2
<a name="python"></a>

 AL2 provides support and security patches for Python 2.7 until June 2026, as part of our long-term support commitment for AL2 core packages. This support extends beyond the upstream Python community declaration of Python 2.7 EOL of January 2020.

**Note**
 AL2023 completely removed Python 2.7. Any components requiring Python are now written to work with Python 3.

 AL2 uses the `yum` package manager that has a hard dependency on Python 2.7. In AL2023, the `dnf` package manager has migrated to Python 3, and no longer requires Python 2.7. AL2023 has completely moved to Python 3. We recommend that you complete your migration to Python 3.
