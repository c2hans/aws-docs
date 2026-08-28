---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/reference-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Reference architecture
<a name="reference-architecture"></a>

The previous section provided a path to migration. This section provides an annotated reference architecture diagram that reinforces these concepts. For a deep dive into the architecture and specific AWS Services that should be used, refer to [Run Semiconductor Design Workflows on AWS](https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/run-semiconductor-design-workflows-on-aws.html).

![Reference architecture diagram depicting semiconductor design on AWS.](http://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/images/semiconductor_ra.png)

*Reference architecture diagram depicting semiconductor design on AWS*

| **Architecture diagram descriptions** |
| --- |
| 1 | Determine what data is needed for proof of concept or test. | 6 | AWS compute is flexible and robust, more than capable of running semiconductor design workflows. |
| 2 | Transfer data into AWS via AWS Snowball, AWS Direct Connect, or using several other AWS services. | 7 | Store tools and job data on Amazon EFS, Amazon FSx for Lustre, and local disk. Optionally, move long-term data storage to Amazon S3. |
| 3 | Transferred data is stored in Amazon S3 buckets. You can access data stored in Amazon S3 from an Amazon EC2 instance or nearly any AWS service. | 8 | Once your data is in AWS, you can leverage other services, such as data lakes, AI/ML, and analytics. |
| 4 | Users access their environment through a remote desktop session or command line (ssh). | 9 | Isolating environments leads to enhanced security and limits third parties to only the data they need. |
| 5 | All of the infrastructure needed for semiconductor design workflows is available on AWS. | 10 | Encryption is everywhere and can be enabled with your encryption keys. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
