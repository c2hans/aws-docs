---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsAccessPoints.html
---

# Working with Amazon S3 on Outposts access points
<a name="S3OutpostsAccessPoints"></a>

To access your Amazon S3 on Outposts bucket, you must create and configure an access point.

Access points simplify managing data access at scale for shared datasets in Amazon S3. Access points are named network endpoints that are attached to buckets that you can use to perform Amazon S3 object operations, such as `GetObject` and `PutObject`. With S3 on Outposts, you must use access points to access any object in an Outposts bucket. Access points support only virtual-host-style addressing.

**Note**
The AWS account that creates the Outposts bucket owns it and is the only one that can assign access points to it.

The following sections describe how to create and manage access points for S3 on Outposts buckets.

**Topics**
+ [Creating an S3 on Outposts access point](S3OutpostsCreateAccessPoint.md)
+ [Using a bucket-style alias for your S3 on Outposts bucket access point](s3-outposts-access-points-alias.md)
+ [Viewing information about an access point configuration](S3OutpostsAccessPointGet.md)
+ [View a list of your Amazon S3 on Outposts access points](S3OutpostsAccessPointList.md)
+ [Deleting an access point](S3OutpostsAccessPointsDelete.md)
+ [Adding or editing an access point policy](S3OutpostsAccessPointEditPolicy.md)
+ [Viewing an access point policy for an S3 on Outposts access point](S3OutpostsAccessPointGetPolicy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
