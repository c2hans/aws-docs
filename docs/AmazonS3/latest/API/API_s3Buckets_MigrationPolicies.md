---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_MigrationPolicies.html
---

# MigrationPolicies
<a name="API_s3Buckets_MigrationPolicies"></a>

The policies for source data that doesn't fit the destination schema.

## Contents
<a name="API_s3Buckets_MigrationPolicies_Contents"></a>

 ** incompatibleValuesPolicy **   <a name="AmazonS3-Type-s3Buckets_MigrationPolicies-incompatibleValuesPolicy"></a>
The migration policy for a source value that the destination column's type can't hold. Valid values:
+  `fail` - Fails the migration. This is the default.
+  `setNull` - Writes null for a value that the destination column's type can't hold. If a column's type in a source object is incompatible with the destination column's type, the column is null for that whole object.
A required column, or a type that migration doesn't support, fails the migration under either value.
Type: String
Valid Values: `fail | setNull`
Required: No

 ** unmatchedSourceFieldsPolicy **   <a name="AmazonS3-Type-s3Buckets_MigrationPolicies-unmatchedSourceFieldsPolicy"></a>
The migration policy for a source field that has no matching column in the destination schema. Valid values:
+  `fail` - Fails the migration. This is the default.
+  `drop` - Leaves source columns that the destination schema doesn't have out of the destination table, and doesn't migrate source objects outside the AWS Glue table's partition locations.
A destination schema that leaves out a partition column or a field of a struct column fails the migration under either value.
Type: String
Valid Values: `fail | drop`
Required: No

## See Also
<a name="API_s3Buckets_MigrationPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/MigrationPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/MigrationPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/MigrationPolicies)
