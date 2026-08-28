---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/configure-videofxprocessor.html
---

# Configuring the VideoFxProcessor object for the Amazon Chime SDK
<a name="configure-videofxprocessor"></a>

The following tables list the `VideoFxProcessor` properties that you can configure. The example below the tables shows a typical runtime configuration.

**Background blur**
Background blur takes the following properties:

| Property | Type | Description |
| --- | --- | --- |
| `isEnabled` | `boolean` | When `true`, the filter blurs the background. |
| `strength` | `string` | Determines the extent of blurring. Valid values: `low` \| `medium` \| `high`. |

**Background replacement**
Background replacement takes the following parameters:

| Property | Type | Description |
| --- | --- | --- |
| `isEnabled` | `boolean` | When `true`, the filter replaces the background. |
| `backgroundImageURL` | `string` | The URL of the background image. The filter resizes the image dynamically to the dimensions of the current screen. You can use a string such as `https://...` or a data URL such as `data:image/jpeg;base64`. |
| `defaultColor` | `string` | A hex color string such as `000000` or `FFFFFF`, or a string such as `black` or `white`. If you don't specify an image URL, the processor uses the `defaultColor` as the background. If you don't specify a `defaultColor` the processor defaults to black. |

**Changing a configuration at runtime**
You can change a `VideoFxProcessor` configuration at runtime by using the `videoFxProcessor.setEffectConfig` parameter. The following example shows how to enable background replacement and disable background blur.

**Note**
You can only specify one type of background replacement at a time. Specify a value for `backgroundImageURL` or `defaultColor`, but not both.

```
videoFxConfig.backgroundBlur.isEnabled = false;
videoFxConfig.backgroundReplacement.isEnabled = true;
try {
  await videoFxProcessor.setEffectConfig(videoFxConfig);
} catch(error) {
  logger.error(error.toString())
}
```

If `setEffectConfig` throws an exception, the previous configuration remains in effect. `setEffectConfig` throws exceptions under conditions similar to those that cause `VideoFxProcessor.create` to throw exceptions.

The following example shows how to change a background image while the video runs.

```
videoFxConfig.backgroundReplacement.backgroundImageURL = "https://{{my-domain.com}}/{{my-other-image.jpg}}";
try {
  await videoFxProcessor.setEffectConfig(videoFxConfig);
} catch(error) {
  logger.error(error.toString())
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
