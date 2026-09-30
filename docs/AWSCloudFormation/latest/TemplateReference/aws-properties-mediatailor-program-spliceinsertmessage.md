---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-spliceinsertmessage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program SpliceInsertMessage
<a name="aws-properties-mediatailor-program-spliceinsertmessage"></a>

Splice insert message configuration.

## Syntax
<a name="aws-properties-mediatailor-program-spliceinsertmessage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-spliceinsertmessage-syntax.json"></a>

```
{
  "[AvailNum](#cfn-mediatailor-program-spliceinsertmessage-availnum)" : {{Integer}},
  "[AvailsExpected](#cfn-mediatailor-program-spliceinsertmessage-availsexpected)" : {{Integer}},
  "[SpliceEventId](#cfn-mediatailor-program-spliceinsertmessage-spliceeventid)" : {{Integer}},
  "[UniqueProgramId](#cfn-mediatailor-program-spliceinsertmessage-uniqueprogramid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-spliceinsertmessage-syntax.yaml"></a>

```
  [AvailNum](#cfn-mediatailor-program-spliceinsertmessage-availnum): {{Integer}}
  [AvailsExpected](#cfn-mediatailor-program-spliceinsertmessage-availsexpected): {{Integer}}
  [SpliceEventId](#cfn-mediatailor-program-spliceinsertmessage-spliceeventid): {{Integer}}
  [UniqueProgramId](#cfn-mediatailor-program-spliceinsertmessage-uniqueprogramid): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-program-spliceinsertmessage-properties"></a>

`AvailNum`  <a name="cfn-mediatailor-program-spliceinsertmessage-availnum"></a>
This is written to `splice_insert.avail_num`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0`. Values must be between `0` and `256`, inclusive.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailsExpected`  <a name="cfn-mediatailor-program-spliceinsertmessage-availsexpected"></a>
This is written to `splice_insert.avails_expected`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0`. Values must be between `0` and `256`, inclusive.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpliceEventId`  <a name="cfn-mediatailor-program-spliceinsertmessage-spliceeventid"></a>
This is written to `splice_insert.splice_event_id`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `1`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UniqueProgramId`  <a name="cfn-mediatailor-program-spliceinsertmessage-uniqueprogramid"></a>
This is written to `splice_insert.unique_program_id`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0`. Values must be between `0` and `256`, inclusive.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
