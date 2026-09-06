---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Namespace.html
---

# Namespace
<a name="API_Namespace"></a>

A collection of database objects and users.

## Contents
<a name="API_Namespace_Contents"></a>

 ** adminPasswordSecretArn **   <a name="redshiftserverless-Type-Namespace-adminPasswordSecretArn"></a>
The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.
Type: String
Required: No

 ** adminPasswordSecretKmsKeyId **   <a name="redshiftserverless-Type-Namespace-adminPasswordSecretKmsKeyId"></a>
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.
Type: String
Required: No

 ** adminUsername **   <a name="redshiftserverless-Type-Namespace-adminUsername"></a>
The username of the administrator for the first database created in the namespace.
Type: String
Required: No

 ** catalogArn **   <a name="redshiftserverless-Type-Namespace-catalogArn"></a>
The Amazon Resource Name (ARN) of the AWS Glue Data Catalog associated with the namespace enabled with Amazon Redshift federated permissions.
Type: String
Required: No

 ** creationDate **   <a name="redshiftserverless-Type-Namespace-creationDate"></a>
The date of when the namespace was created.
Type: Timestamp
Required: No

 ** dbName **   <a name="redshiftserverless-Type-Namespace-dbName"></a>
The name of the first database created in the namespace.
Type: String
Required: No

 ** defaultIamRoleArn **   <a name="redshiftserverless-Type-Namespace-defaultIamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
Type: String
Required: No

 ** iamRoles **   <a name="redshiftserverless-Type-Namespace-iamRoles"></a>
A list of IAM roles to associate with the namespace.
Type: Array of strings
Required: No

 ** kmsKeyId **   <a name="redshiftserverless-Type-Namespace-kmsKeyId"></a>
The ID of the AWS Key Management Service key used to encrypt your data.
Type: String
Required: No

 ** lakehouseRegistrationStatus **   <a name="redshiftserverless-Type-Namespace-lakehouseRegistrationStatus"></a>
The status of the lakehouse registration for the namespace. Indicates whether the namespace is successfully registered with Amazon Redshift federated permissions.
Type: String
Required: No

 ** logExports **   <a name="redshiftserverless-Type-Namespace-logExports"></a>
The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Valid Values: `useractivitylog | userlog | connectionlog`
Required: No

 ** namespaceArn **   <a name="redshiftserverless-Type-Namespace-namespaceArn"></a>
The Amazon Resource Name (ARN) associated with a namespace.
Type: String
Required: No

 ** namespaceId **   <a name="redshiftserverless-Type-Namespace-namespaceId"></a>
The unique identifier of a namespace.
Type: String
Required: No

 ** namespaceName **   <a name="redshiftserverless-Type-Namespace-namespaceName"></a>
The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** status **   <a name="redshiftserverless-Type-Namespace-status"></a>
The status of the namespace.
Type: String
Valid Values: `AVAILABLE | MODIFYING | DELETING`
Required: No

## See Also
<a name="API_Namespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/Namespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/Namespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/Namespace)
