---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/advanced-knowledge-base-settings.html
---

# Advanced knowledge base settings
<a name="advanced-knowledge-base-settings"></a>

Advanced Knowledge Base Settings such as Knowledge Base Filtering and RAG with Role Based Access Control are available for use with the solution. Knowledge Base Filtering can apply to either of the Knowledge Bases while RAG with Role Based Access Control is specifically available for Amazon Kendra.

## Knowledge base filtering
<a name="knowledge-base-filtering"></a>

The solution allows you to specify [Amazon Kendra attribute filters](https://docs.aws.amazon.com/kendra/latest/APIReference/API_AttributeFilter.html) or [Bedrock knowledge base retrieval filters](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) when deploying a use case in the Advanced RAG configurations section of the wizards knowledge base step. These filters define how data sources in the knowledge base are queried, such as search strategies, languages of the underlying document being queries, etc.

In both cases, a JSON object is used to specify the filter settings per the format specified in each services documentation (as linked above).

 *Example 1: Kendra AttributeFilter*

```
{
 "EqualsTo": {
 "Key": "_language_code",
 "Value": {
 "StringValue": "es"
 }
 }
}
```

 *Example 2: Bedrock RetrievalFilter*

```
{
 "equals": {
 "key": "language",
 "value": "es"
 }
}
```

## RAG with Role Based Access Control with Amazon Kendra
<a name="rag-rbac-with-kendra"></a>

 [Role-based access control (RBAC)](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control.html) allows controlling which users or groups can access certain documents in your Amazon Kendra index or see certain documents in their search results. To configure RBAC for your Amazon Kendra Index ID with your Generative AI Application Builder on AWS (GAAB) use case, follow these steps:

 **1. Configure Amazon Kendra Index**

1. Ensure that you have an Amazon Kendra index created and at least one data source added to it.

1. Configure access control for your data source based on user groups. For an S3 data source, follow the [instructions available in the documentation](https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html) to set up access control lists (ACLs) using the same group names created in your Amazon Cognito User Pool. This ensures that users can only access the documents and search results they are authorized to view based on their group membership.

**Note**
Under **User Access Control** in the Kendra Index you created, leave **Token-based user access control** as **No**. When you enable **Role Based Access Control** in Step 2, Generative AI Application Builder on AWS extracts the appropriate claims from the user authentication token and creates an Attribute Filter.

 **2. Deploy RAG Use Case using GAAB Deployment Wizard**

1. Follow the on-screen wizard instructions in the GAAB Deployment Wizard until you reach step 4 of the wizard to configure RAG.

1. In the **Select Knowledge Base** step of the deployment wizard, choose **Amazon Kendra** as the knowledge base type.

1. Specify whether you have an existing Amazon Kendra index or if you want to create a new one. If you have an existing index, provide the ID of your Amazon Kendra index that has been configured with access control lists (ACLs) based on user groups.

1. Enable the **Role Based Access Control** option. This option ensures that the search results returned from the Amazon Kendra index are filtered based on the user’s role and group permissions.

1. Review and deploy the use case.

 **3. Configure Amazon Cognito**

1. Locate the Amazon Cognito User Pool used by your GAAB deployment. This Amazon Cognito User Pool is typically created by the main deployment dashboard CloudFormation stack.

1. Create new users in the Amazon Cognito User Pool. When creating users, select the 'Send an email invitation' option so that users receive temporary login credentials via email. This allows new users to sign up and access the GAAB application.

1. Create user groups in the Amazon Cognito User Pool. Ensure that the group names exactly match the groups configured in your Amazon Kendra index ACLs. This is crucial for enabling RBAC, as the user’s group membership will determine the search results they can access.

1. Assign users to the appropriate groups based on their roles and access permissions. Users must be added to both the group required for the Amazon Kendra index ACL, as well as the use case-specific group created during the GAAB deployment. This ensures that users have the necessary permissions to access the specific use case and the relevant search results.

By following these steps, you will have configured role-based access control (RBAC) for your GAAB deployment, ensuring that users can only access and interact with the information and features they are authorized for, based on their assigned user group and permissions.

**Note**
As of now, only Amazon Kendra supports RBAC for knowledge bases in the Generative AI Application Builder on AWS. For Amazon Bedrock Knowledge Base, RBAC is not supported, but you can use metadata filters to achieve some level of filtering. For more information, refer to the [Amazon Bedrock User Guide.](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
