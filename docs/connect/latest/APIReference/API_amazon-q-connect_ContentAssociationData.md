---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ContentAssociationData.html
---

# ContentAssociationData
<a name="API_amazon-q-connect_ContentAssociationData"></a>

Information about the content association.

## Contents
<a name="API_amazon-q-connect_ContentAssociationData_Contents"></a>

 ** associationData **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-associationData"></a>
The content association.
Type: [ContentAssociationContents](API_amazon-q-connect_ContentAssociationContents.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** associationType **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-associationType"></a>
The type of association.
Type: String
Valid Values: `AMAZON_CONNECT_GUIDE`
Required: Yes

 ** contentArn **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-contentArn"></a>
The Amazon Resource Name (ARN) of the content.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** contentAssociationArn **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-contentAssociationArn"></a>
The Amazon Resource Name (ARN) of the content association.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** contentAssociationId **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-contentAssociationId"></a>
The identifier of the content association. Can be either the ID or the ARN. URLs cannot contain the ARN.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** contentId **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-contentId"></a>
The identifier of the content.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** tags **   <a name="connect-Type-amazon-q-connect_ContentAssociationData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_ContentAssociationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ContentAssociationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ContentAssociationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ContentAssociationData)
