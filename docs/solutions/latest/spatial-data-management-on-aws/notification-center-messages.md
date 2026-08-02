---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-messages.html
---

# Message templates
<a name="notification-center-messages"></a>

By default, SDMA generates the notification message as `"{resourceName} — {eventName}"` (for example, `"My Asset — Asset Created"`). To customize the message, add a `messages` field to the notification rule configuration.

Messages support variable interpolation. The built-in variable `${eventName}` resolves to a human-readable label for the triggering event, such as `"Asset Created"`, `"File Uploaded"`, or `"State Changed"`. All standard SDMA field variables are also available — `${asset.assetName}`, `${project.projectName}`, `${file.path}`, and so on.

Example:

```
"messages": ["${asset.assetName} - ${eventName}"]
```

Multiple messages are concatenated with newlines in the notification body:

```
"messages": ["Asset ${asset.assetName} — ${eventName}", "Project: ${project.projectName}"]
```

You can also define different messages per resource type using an object format. When an event fires, the array matching the resource type is used. If no match, the `"default"` key is used:

```
"messages": {
  "asset": ["Asset ${asset.assetName} (${asset.assetId}) — ${eventName}"],
  "project": ["Project ${project.projectName} — ${eventName}"],
  "file": ["File ${file.path} — ${eventName}", "Asset: ${asset.assetName}"],
  "default": ["${eventName} notification"]
}
```

Messages are shared across all channels — define them once at the rule level, not inside individual channel configurations.
