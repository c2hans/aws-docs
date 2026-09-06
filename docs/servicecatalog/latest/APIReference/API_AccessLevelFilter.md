---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AccessLevelFilter.html
---

# AccessLevelFilter
<a name="API_AccessLevelFilter"></a>

The access level to use to filter results.

## Contents
<a name="API_AccessLevelFilter_Contents"></a>

 ** Key **   <a name="servicecatalog-Type-AccessLevelFilter-Key"></a>
The access level.
+  `Account` - Filter results based on the account.
+  `Role` - Filter results based on the federated role of the specified user.
+  `User` - Filter results based on the specified user.
Type: String
Valid Values: `Account | Role | User`
Required: No

 ** Value **   <a name="servicecatalog-Type-AccessLevelFilter-Value"></a>
The user to which the access level applies. The only supported value is `self`.
Type: String
Required: No

## See Also
<a name="API_AccessLevelFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/AccessLevelFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/AccessLevelFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/AccessLevelFilter)
