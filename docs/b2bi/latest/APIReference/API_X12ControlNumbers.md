---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ControlNumbers.html
---

# X12ControlNumbers
<a name="API_X12ControlNumbers"></a>

Contains configuration for X12 control numbers used in X12 EDI generation. Control numbers are used to uniquely identify interchanges, functional groups, and transaction sets.

## Contents
<a name="API_X12ControlNumbers_Contents"></a>

 ** startingFunctionalGroupControlNumber **   <a name="b2bi-Type-X12ControlNumbers-startingFunctionalGroupControlNumber"></a>
Specifies the starting functional group control number (GS06) to use for X12 EDI generation. This number is incremented for each new functional group. For the GS (functional group) envelope, AWS B2B Data Interchange generates a functional group control number that is unique to the sender ID, receiver ID, and functional identifier code combination.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** startingInterchangeControlNumber **   <a name="b2bi-Type-X12ControlNumbers-startingInterchangeControlNumber"></a>
Specifies the starting interchange control number (ISA13) to use for X12 EDI generation. This number is incremented for each new interchange. For the ISA (interchange) envelope, AWS B2B Data Interchange generates an interchange control number that is unique for the ISA05 and ISA06 (sender) & ISA07 and ISA08 (receiver) combination.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

 ** startingTransactionSetControlNumber **   <a name="b2bi-Type-X12ControlNumbers-startingTransactionSetControlNumber"></a>
Specifies the starting transaction set control number (ST02) to use for X12 EDI generation. This number is incremented for each new transaction set.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: No

## See Also
<a name="API_X12ControlNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12ControlNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12ControlNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12ControlNumbers)
