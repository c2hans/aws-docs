---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migration-patterns-and-architectures.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration patterns and architectures
<a name="migration-patterns-and-architectures"></a>

 This section describes, at a high level, how corporate on-premises customers can migrate Oracle E-Business Suite to the AWS Cloud.

![Diagram showing a representative Oracle E-Business Suite migration approach](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/migration-approach.png)

**Sequence:**

1.  Replicate database from on-premises to Clone database. Technology options include:
   +  Oracle Data Guard
   +  Physical Standby
   +  RMAN
   +  Transportable Tablespaces
   +  DataPump
   +  [AWS Snowball Edge](https://aws.amazon.com/snowball/)
   + [AWS Transform MGN](https://aws.amazon.com/application-migration-service/)

1.  Establish replication from on premises to AWS

1.  Replicate application files from on-premises to AWS filesystem. For shared filesystem, options include Amazon EFS, or FSx NetApp ONTAP.

    Technology options include:
   + `rsync` (lift and shift / incremental)
   + `tar` (lift and shift)
   + Fresh Rapidwiz install
   + AWS Transform MGN
   + AWS DataSync

1.  Configure target database and application with PostClone and Autoconfig

1.  DNS Configuration (Amazon Route 53) switching users to Application Load Balancer

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
