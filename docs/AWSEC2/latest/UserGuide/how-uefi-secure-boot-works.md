---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-uefi-secure-boot-works.html
---

# How UEFI Secure Boot works with Amazon EC2 instances
<a name="how-uefi-secure-boot-works"></a>

UEFI Secure Boot is a feature specified in UEFI, which provides verification about the state of the boot chain. It is designed to ensure that only cryptographically verified UEFI binaries are executed after the self-initialization of the firmware. These binaries include UEFI drivers and the main bootloader, as well as chain-loaded components.

UEFI Secure Boot specifies four key databases, which are used in a chain of trust. The databases are stored in the UEFI variable store.

The chain of trust is as follows:

**Platform key (PK) database**
The PK database is the root of trust. It contains a single public PK key that is used in the chain of trust for updating the key exchange key (KEK) database.
To change the PK database, you must have the private PK key to sign an update request. This includes deleting the PK database by writing an empty PK key.

**Key exchange key (KEK) database**
The KEK database is a list of public KEK keys that are used in the chain of trust for updating the signature (db) and denylist (dbx) databases.
To change the public KEK database, you must have the private PK key to sign an update request.

**Signature (db) database**
The db database is a list of public keys and hashes that are used in the chain of trust to validate all UEFI boot binaries.
To change the db database, you must have the private PK key or any of the private KEK keys to sign an update request.

**Signature denylist (dbx) database**
The dbx database is a list of public keys and binary hashes that are not trusted, and are used in the chain of trust as a revocation file.
The dbx database always takes precedence over all other key databases.
To change the dbx database, you must have the private PK key or any of the private KEK keys to sign an update request.
The UEFI Forum maintains a publicly available dbx for many known-bad binaries and certs at [https://uefi.org/revocationlistfile](https://uefi.org/revocationlistfile).

**Important**
UEFI Secure Boot enforces signature validation on any UEFI binaries. To permit execution of a UEFI binary in UEFI Secure Boot, you sign it with any of the private db keys described above.

By default, UEFI Secure Boot is disabled and the system is in `SetupMode`. When the system is in `SetupMode`, all key variables can be updated without a cryptographic signature. When the PK is set, UEFI Secure Boot is enabled and the SetupMode is exited.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
