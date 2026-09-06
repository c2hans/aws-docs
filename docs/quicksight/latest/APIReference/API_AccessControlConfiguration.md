---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccessControlConfiguration.html
---

# AccessControlConfiguration
<a name="API_AccessControlConfiguration"></a>

The access control settings for a knowledge base. Use this structure to enable or disable document-level access control lists (ACLs) that filter query results based on the permissions from the source data connector.

## Contents
<a name="API_AccessControlConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** isACLEnabled **   <a name="QS-Type-AccessControlConfiguration-isACLEnabled"></a>
Specifies whether ACLs are enabled for the knowledge base.
This setting works together with the data source connector's ACL crawling. To enforce document-level access control end to end, set `isACLEnabled` to `true` and enable ACL crawling on the connector. For example, for an Amazon S3 data source, set `accessControlConfiguration.crawlAcl` to `true` in the connector template. For more information, see `KbTemplateConfiguration`. Enabling only one of the two settings does not produce a fully ACL-enforced knowledge base.
Type: Boolean
Required: No

## See Also
<a name="API_AccessControlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AccessControlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AccessControlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AccessControlConfiguration)
