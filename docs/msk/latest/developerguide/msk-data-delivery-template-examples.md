---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-template-examples.html
---

# Examples
<a name="msk-data-delivery-template-examples"></a>

## Valid
<a name="msk-data-delivery-template-examples-valid"></a>

```
!{channel-id}/!{yyyy}/!{MM}/!{dd}/!{sequence-number}
topic=!{topic-name}/!{partition-id}/!{kafka-offset}
!{partition-id}-!{kafka-offset}
data/!{channel-id}/!{HH}/!{sequence-number}.json
```

## Invalid
<a name="msk-data-delivery-template-examples-invalid"></a>

| Template | Why it fails |
| --- | --- |
| `!{yyyy}/!{MM}/` | Ends with `/` |
| `!{channel-id}/!{topic-name}` | No `sequence-number` or `kafka-offset` |
| `!{sequence-number}-!{kafka-offset}` | Both present (mutually exclusive) |
| `!{kafka-offset}` | `kafka-offset` without `partition-id` |
| `!{sequence-number}/literal-tail` | Uniqueness token not in the last segment |
| `!{badvar}/!{sequence-number}` | Unknown variable |
| `foo bar/!{sequence-number}` | Space is not an allowed literal character |
