---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/put-acl-permissions-ap.html
---

# Configure access control lists (ACLs) through an access point for a general purpose bucket
<a name="put-acl-permissions-ap"></a>

This section explains how to configure ACLs through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API. For more information about ACLs, see [Access control list (ACL) overview](acl-overview.md).

## Using the S3 console
<a name="put-acl-permissions-ap-console"></a>

**To configure ACLs through an access point in your AWS account**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to list access points for.

1. In the navigation pane on the left side of the console, choose **Access Points**.

1. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.

1. Choose the name of the access point you want to manage or use.

1. Under the **Objects** tab, select the name of the object you wish to configure an ACL for.

1. Under the **Permissions** tab, select **Edit** to configure the object ACL.
**Note**
Amazon S3 currently doesn't support changing an access point's block public access settings after the access point has been created.

## Using the AWS CLI
<a name="put-acl-permissions-ap-cli"></a>

The following `put-object-acl` example command shows how you can use the AWS CLI to configure access permissions through an access point using an ACL.

The following command applies an ACL to an existing object `puppy.jpg` through an access point owned by AWS account {{111122223333}}.

```
aws s3api put-object-acl --bucket arn:aws:s3:{{AWS Region}}:111122223333:accesspoint/{{my-access-point}} --key puppy.jpg --acl private
```

**Note**
S3 automatically generate access point aliases for all access points and these aliases can be used anywhere a bucket name is used to perform object-level operations. For more information, see [Access point aliases](access-points-naming.md#access-points-alias).

For more information and examples, see [put-object-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-acl.html) in the *AWS CLI Command Reference*.

## Using the REST API
<a name="put-acl-permissions-ap-rest"></a>

You can use the REST API to configure access permissions through an access point using an ACL. For more information, see [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) in the *Amazon Simple Storage Service API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
