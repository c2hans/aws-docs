---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DiffChange.html
---

# DiffChange
<a name="API_DiffChange"></a>

A single line-level entry in a diff hunk. Each `DiffChange` describes one line and its change type: unchanged context, an addition in the after blob, or a deletion from the before blob.

## Contents
<a name="API_DiffChange_Contents"></a>

 ** afterLineNumber **   <a name="CodeCommit-Type-DiffChange-afterLineNumber"></a>
The 1-based line number in the after blob. This field is omitted for `DELETE` lines.
Type: Integer
Required: No

 ** beforeLineNumber **   <a name="CodeCommit-Type-DiffChange-beforeLineNumber"></a>
The 1-based line number in the before blob. This field is omitted for `ADD` lines.
Type: Integer
Required: No

 ** content **   <a name="CodeCommit-Type-DiffChange-content"></a>
The text content of the line, without the trailing newline.
Type: String
Required: No

 ** type **   <a name="CodeCommit-Type-DiffChange-type"></a>
The type of change for this line. Possible values:
+  `CONTEXT` – Unchanged line included for surrounding context.
+  `ADD` – Line added in the after blob.
+  `DELETE` – Line removed from the before blob.
Type: String
Valid Values: `CONTEXT | ADD | DELETE`
Required: No

## See Also
<a name="API_DiffChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DiffChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DiffChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DiffChange)
