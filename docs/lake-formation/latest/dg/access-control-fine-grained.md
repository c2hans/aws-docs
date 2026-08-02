---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-fine-grained.html
---

# Methods for fine-grained access control
<a name="access-control-fine-grained"></a>

With a data lake, the goal is to have fine-grained access control to data. In Lake Formation, this means fine-grained access control to Data Catalog resources and Amazon S3 locations. You can achieve fine-grained access control with one of the following methods.

| Method | Lake Formation Permissions | IAM Permissions | Comments |
| --- | --- | --- | --- |
| Method 1 | Open | Fine-grained | **This is the default method** for backward compatibility with AWS Glue.[See the AWS documentation website for more details](http://docs.aws.amazon.com/lake-formation/latest/dg/access-control-fine-grained.html)<br />On the Lake Formation console, this method appears as **Use only IAM access control**. |
| Method 2 | Fine-grained | Coarse-grained | **This is the recommended method.**[See the AWS documentation website for more details](http://docs.aws.amazon.com/lake-formation/latest/dg/access-control-fine-grained.html) |

**Important**
Be aware of the following:
By default, Lake Formation has the **Use only IAM access control** settings enabled for compatibility with existing AWS Glue Data Catalog behavior. We recommend that you disable these settings after you transition to using Lake Formation permissions. For more information, see [Changing the default settings for your data lake](change-settings.md).
Data lake administrators and database creators have implicit Lake Formation permissions that you must understand. For more information, see [Implicit Lake Formation permissions](implicit-permissions.md).
