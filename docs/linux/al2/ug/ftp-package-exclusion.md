---
source_url: https://docs.aws.amazon.com/linux/al2/ug/ftp-package-exclusion.html
---

# `ftp` Package
<a name="ftp-package-exclusion"></a>

The `ftp` package in AL2 is no longer available in Amazon Linux starting with AL2023. This decision was made as part of our ongoing commitment to security, maintainability, and modern software development practices. As part of (or before) migrating to AL2023, we recommend migrating any use of the legacy `ftp` package to one of its alternatives.

## Background
<a name="ftp-package-background"></a>

The legacy `ftp` package has not been actively maintained upstream for many years. The last significant update to the source code occurred in the early 2000s, and the original source repository is no longer available. While some Linux distributions have carried patches for security vulnerabilities, the codebase remains largely unmaintained.

## Recommended Alternatives
<a name="ftp-package-alternatives"></a>

AL2023 provides several modern, actively maintained alternatives for FTP functionality:

`lftp` (available in AL2 and AL2023)
A sophisticated file transfer program supporting FTP, HTTP, SFTP, and other protocols. It offers more features than the traditional `ftp` client and is actively maintained.
Install with: **dnf install lftp**

`curl` (available in AL2 and AL2023)
A versatile command-line tool for transferring data with URLs, supporting FTP, FTPS, HTTP, HTTPS, and many other protocols.
Available by default in AL2023 via the `curl-minimal` package. For more extensive protocol support, you can optionally upgrade to `curl-full` using **dnf swap curl-minimal curl-full**.

`wget` (available in AL2 and AL2023)
A non-interactive command-line utility for downloading files from the web, supporting HTTP, HTTPS, and FTP protocols.
Install with: **dnf install wget** (not installed by default in all AL2023 images)

`sftp` (available in AL2 and AL2023)
A secure file transfer protocol that operates over SSH, providing encrypted file transfers.
Available by default as part of the OpenSSH package.

## Migration Considerations
<a name="ftp-package-migration"></a>

If your applications or scripts depend on the legacy `ftp` client, consider the following migration approaches:

1. **Update scripts to use modern alternatives**: Modify your scripts to use `lftp`, `curl`, `wget`, or `sftp` instead of the legacy `ftp` client.

1. **Review package dependencies**: Some applications may list the `ftp` package as a dependency in their package metadata, even though they have long since migrated to using modern protocols internally. In these cases, the application may work correctly on AL2023 despite the lack of `/usr/bin/ftp` from the `ftp` package. Review your application's actual requirements rather than relying solely on stated dependencies.

1. **Update application dependencies**: For applications you maintain that still declare a dependency on the `ftp` package but don't actually use it, update the package metadata to remove this unnecessary dependency.

## Security Considerations
<a name="ftp-package-security"></a>

The FTP protocol transmits data, including authentication credentials, in plaintext. For security-sensitive applications, we strongly recommend using encrypted alternatives such as SFTP or HTTPS which are supported by the recommended alternative tools.
