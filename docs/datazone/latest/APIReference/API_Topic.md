---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_Topic.html
---

# Topic
<a name="API_Topic"></a>

The topic of the notification.

## Contents
<a name="API_Topic_Contents"></a>

 ** resource **   <a name="datazone-Type-Topic-resource"></a>
The details of the resource mentioned in a notification.
Type: [NotificationResource](API_NotificationResource.md) object
Required: Yes

 ** role **   <a name="datazone-Type-Topic-role"></a>
The role of the resource mentioned in a notification.
Type: String
Valid Values: `PROJECT_OWNER | PROJECT_CONTRIBUTOR | PROJECT_VIEWER | DOMAIN_OWNER | PROJECT_SUBSCRIBER`
Required: Yes

 ** subject **   <a name="datazone-Type-Topic-subject"></a>
The subject of the resource mentioned in a notification.
Type: String
Required: Yes

## See Also
<a name="API_Topic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/Topic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/Topic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/Topic)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
