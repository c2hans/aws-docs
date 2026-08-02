---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-videofxconfig.html
---

# Creating a VideoFxConfig object for the Amazon Chime SDK
<a name="create-videofxconfig"></a>

You can define configurations for `backgroundBlur` and `backgroundReplacement` in the same object. However, you can't set `isEnabled` to `true` for both filters at the same time. That's an invalid configuration.

The `VideoFxConfig` class does no validation of its own. Validation occurs in the next step.

The following example shows a valid `VideoFxConfig`.

```
const videoFxConfig: VideoFxConfig = {
    backgroundBlur: {
        isEnabled: {{false}},
        strength: '{{medium}}'
    },
    backgroundReplacement: {
        isEnabled: {{false}},
        backgroundImageURL: '{{space.jpg}}',
        defaultColor: {{undefined}},
    }
}
```

The following tables list the `VideoFxProcessor` properties that you can specify in the `VideoFxConfig` object.

**Background blur filter properties**

| Property | Type | Description |
| --- | --- | --- |
| `isEnabled` | `boolean` |  When `true`, the filter blurs the background. |
| `strength` | `string` | Determines the extent of blurring. Valid values: `low` \| `medium` \| `high`. |

**Background replacement filter properties**

| Property | Type | Description |
| --- | --- | --- |
| `isEnabled` | `boolean` |  When `true`, the filter replaces the background\\. |
| `backgroundImageURL` | `string` | The URL of the background image. The filter resizes the image dynamically to the dimensions of the current screen. You can use a string such as `https://...` or a data URL such as `data:image/jpeg;base64`. |
| `defaultColor` | `string` | A hex color string such as `000000` or `FFFFFF`, or a string such as `black` or `white`. If you don't specify an image URL, the processor uses the `defaultColor` as the background. If you don't specify a `defaultColor`, the processor defaults to black. |
