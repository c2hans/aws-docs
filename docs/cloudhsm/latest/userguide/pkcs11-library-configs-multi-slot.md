---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-library-configs-multi-slot.html
---

# Multiple slot configuration with PKCS \#11 library for AWS CloudHSM
<a name="pkcs11-library-configs-multi-slot"></a>

A single slot in Client SDK 5 PKCS \#11 library represents a single connection to a cluster in AWS CloudHSM. With Client SDK 5, you can configure your PKCS11 library to allow multiple slots to connect users to multiple CloudHSM clusters from a single PKCS\#11 application.

Use the instructions in this topic to make your application use multi-slot functionality to connect with multiple clusters.

**Topics**
+ [Multi-slot prerequisites for PKCS \#11 library for AWS CloudHSM](#pkcs11-multi-slot-prereqs)
+ [Configure the PKCS \#11 library for multi-slot functionality for AWS CloudHSM](pkcs11-multi-slot-config-run.md)
+ [Add a cluster with multi-slot functionality for AWS CloudHSM](pkcs11-multi-slot-add-cluster.md)
+ [Remove a cluster with multi-slot functionality for AWS CloudHSM](pkcs11-multi-slot-remove-cluster.md)

## Multi-slot prerequisites for PKCS \#11 library for AWS CloudHSM
<a name="pkcs11-multi-slot-prereqs"></a>

Before configuring for multiple slots for PKCS \#11 library for AWS CloudHSM, complete the following prerequisites.
+ Two or more AWS CloudHSM clusters to which you’d like to connect to, along with their cluster certificates.
+ An EC2 instance with Security Groups correctly configured to connect to all of the clusters above. For more information about how to set up a cluster and the client instance, refer to [Getting started with AWS CloudHSM](getting-started.md).
+ To set up multi-slot functionality, you must have already downloaded and installed the PKCS \#11 library. If you have not already done this, refer to the instructions in [Install the PKCS \#11 library for AWS CloudHSM Client SDK 5](pkcs11-library-install.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
