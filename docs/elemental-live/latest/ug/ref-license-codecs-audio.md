---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/ref-license-codecs-audio.html
---

# Add-on packages for audio codecs
<a name="ref-license-codecs-audio"></a>

Some audio codecs require an add-on package. This table lists audio codecs in alphabetical order. Each row identifies whether Elemental Live requires an add-on package to decode an audio source that uses this codec, to pass through the audio source to the output, or to encode an output with this codec.

- ** Dolby Digital   **
  - **Action:** Decode or passthrough  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**
  - **Action:** Encode  / **Add-on Package:** Advanced Audio Package  / **Change on Web Interface:** The codec appears as an option in the **Audio Codec** field in the relevant outputs. To find the field in the event, go to an Output Groups tab. In that tab, go to the Outputs section, then to the Streams section. Choose Audio. The field appears on the first line.

- ** Dolby Digital Plus    **
  - **Action:** Decode  / **Add-on Package:** Audio Decoder Package  / **Change on Web Interface:** There is no change in the input section of an event, but Elemental Live will ingest a **Dolby Digital Plus** audio source.
  - **Action:** Passthrough  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**
  - **Action:** Encode  / **Add-on Package:** Advanced Audio Package  / **Change on Web Interface:** The codec appears as an option in the **Audio Codec** field in the relevant outputs. To find the field in the event, go to an Output Groups tab. In that tab, go to the Outputs section, then to the Streams section. Choose Audio. The field appears on the first line.

- ** Dolby E    **
  - **Action:** Decode  / **Add-on Package:** Audio Decoder Package  / **Change on Web Interface:** The **Dolby E Program Selection** field appears for an event. To find the field in the event, go to an Output Groups tab. In that tab, go to the Outputs section, then to the Streams section. Choose Audio. The field appears on the first line.
  - **Action:** Passthrough  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**
  - **Action:** Encode  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**

- ** Dolby Digital Plus with Atmos    **
  - **Action:** Decode  / **Add-on Package:** Decode isn't supported  / **Change on Web Interface:**
  - **Action:** Passthrough  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**
  - **Action:** Encode  / **Add-on Package:** Advanced Audio Package  / **Change on Web Interface:** The codec appears as an option in the **Audio Codec** field in the relevant outputs. To find the field in the event, go to an Output Groups tab. In that tab, go to the Outputs section, then to the Streams section. Choose Audio. The field appears on the first line.

- ** DTS Express **
  - **Action:** Decode  / **Add-on Package:** Decode isn't supported  / **Change on Web Interface:**
  - **Action:** Passthrough  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**
  - **Action:** Encode  / **Add-on Package:** Advanced Audio Package  / **Change on Web Interface:** The codec appears as an option in the **Audio Codec** field in the relevant outputs. To find the field in the event, go to an Output Groups tab. In that tab, go to the Outputs section, then to the Streams section. Choose Audio. The field appears on the first line.

- ** Other audio codecs    **
  - **Action:** Decode  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**
  - **Action:** Passthrough  / **Add-on Package:** Passthrough isn't supported / **Change on Web Interface:**
  - **Action:** Encode  / **Add-on Package:** No add-on package required  / **Change on Web Interface:**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
