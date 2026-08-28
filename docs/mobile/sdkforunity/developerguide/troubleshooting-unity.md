---
source_url: https://docs.aws.amazon.com/mobile/sdkforunity/developerguide/troubleshooting-unity.html
---

The AWS Mobile SDK for Unity is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Unity. For more information, see [What is the AWS Mobile SDK for Unity?](what-is-unity-plugin.md)

# Troubleshooting
<a name="troubleshooting-unity"></a>

Due to limitations of the Unity.WWW class used by the AWS SDK for Unity, detailed error messages are not returned when a problem occurs while calling an AWS service. This topic describes some ideas for troubleshooting such problems.

## Ensure IAM Role Has Required Permissions
<a name="ensure-iam-role-has-required-permissions"></a>

When calling AWS services your app uses an identity from a Cognito identity pool. Each identity in the pool is associated with an IAM (Identity and Access Management) role. The role has one or more policy files associated with it that specify what AWS resources the users assigned to the role have access to. By default two roles are created, one for authenticated users, and one for unauthenticated users. You will need to either modify the existing policy file or associate a new policy file with the permisssions required by your app. If your app allows both authenticated and unauthenticated users, both roles must be granted permissions for accessing the AWS resources your app needs.

The following policy file shows how to grant access to an S3 bucket:

```
{
  "Statement": [
    {
      "Action": [
        "s3:AbortMultipartUpload",
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::MYBUCKETNAME/*",
      "Principal": "*"
    }
  ]
}
```

The following policy file shows how to grant access to a DynamoDB database:

```
{
"Statement": [{
    "Effect": "Allow",
    "Action": [
        "dynamodb:DeleteItem",
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:Scan",
        "dynamodb:UpdateItem"
    ],
    "Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/MyTable"
}]
}
```

For more information about specifying policies, see [IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html).

## Using a HTTP Proxy Debugger
<a name="using-a-http-proxy-debugger"></a>

If the AWS service your app is calling has an HTTP or HTTPS endpoint, you can use an HTTP/HTTPS proxy debugger to view the requests and responsese to gain more insight into what is occuring. There are a number of HTTP proxy debuggers available such as:
+  [Charles](http://www.charlesproxy.com/) - a web debugging proxy for OSX
+  [Fiddler](http://www.telerik.com/fiddler) - a web debugging proxyfidd for Windows

**Important**
There is a known issue with the Cognito Credential Provider when running the Charles web debugging proxy that prevents the credential provider from working correctly.

Both Charles and Fiddler require some configuration to be able to view SSL encrypted traffic, please read the documentation for these tools for further information. If you are using a web debugging proxy that cannot be configured to display encrypted traffic, open the aws\_endpoints\_json file (located in AWSUnitySDK/AWSCore/Resources) and set the HTTP tag for the AWS service you need to debug to true

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mobile SDK for Unity. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mobile` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
