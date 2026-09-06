---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tagging.html
---

# Tag your Amazon Location Service resources
<a name="tagging"></a>

Use resource tagging in Amazon Location to create tags to categorize your resources by purpose, owner, environment, or criteria. Tagging your resources helps you manage, identify, organize, search, and filter your resources.

For example, with AWS Resource Groups, you can create groups of AWS resources based on one or more tags or portions of tags. You can also create groups based on their occurrence in an CloudFormation stack. Using Resource Groups and Tag Editor, you can consolidate and view data for applications that consist of multiple services, resources, and Regions in one place. For more information on [Common Tagging Strategies](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-strategies), see the *AWS General Reference*.

Each tag is a label consisting of a key and value that you define:
+ **Tag key** – A general label that categorizes the tag values. For example, `CostCenter`.
+ **Tag value** – An optional description for the tag key category. For example, `MobileAssetTrackingResourcesProd`.

This topic helps you get started with tagging by reviewing tagging restrictions. It also shows you how to create tags and use tags to track your AWS cost for each active tag by using cost allocation reports.

For more information about:
+ Tagging best practices, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-best-practices) in the *AWS General Reference*.
+ Using tags to control access to AWS resources, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *AWS Identity and Access Management User Guide*.
