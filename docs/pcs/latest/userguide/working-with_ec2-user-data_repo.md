---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data_repo.html
---

# Example: Install software for AWS PCS from a package repository
<a name="working-with_ec2-user-data_repo"></a>

 Provide this script as the value of `"userData"` in your launch template. For more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md).

This script uses **cloud-config** to install software packages on node group instances at launch. For more information, see the [User data formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the *cloud-init documentation*. This example installs `curl` and `llvm`.

**Note**
Your instances must be able to connect to their configured package repositories.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
- python3-devel
- rust
- golang

--==MYBOUNDARY==--
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
