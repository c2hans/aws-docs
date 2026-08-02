---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTableWitnessDescription.html
---

# GlobalTableWitnessDescription
<a name="API_GlobalTableWitnessDescription"></a>

Represents the properties of a witness Region in a MRSC global table.

## Contents
<a name="API_GlobalTableWitnessDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-GlobalTableWitnessDescription-RegionName"></a>
The name of the AWS Region that serves as a witness for the MRSC global table.
Type: String
Required: No

 ** WitnessStatus **   <a name="DDB-Type-GlobalTableWitnessDescription-WitnessStatus"></a>
The current status of the witness Region in the MRSC global table.
Type: String
Valid Values: `CREATING | DELETING | ACTIVE`
Required: No

## See Also
<a name="API_GlobalTableWitnessDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalTableWitnessDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalTableWitnessDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalTableWitnessDescription)
