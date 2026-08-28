---
source_url: https://docs.aws.amazon.com/transcribe/latest/dg/how-measurements-med.html
---

# Transcribing medical terms and measurements
<a name="how-measurements-med"></a>

Amazon Transcribe Medical can transcribe medical terms and measurements. Amazon Transcribe Medical outputs abbreviations for spoken terms. For example, "blood pressure" is transcribed as BP. You can find a list of conventions that Amazon Transcribe Medical uses for medical terms and measurements in the table on this page. The *Spoken Term* column refers to the term spoken in the source audio. The *Output* column refers to the abbreviation you see in your transcription results.

You can see how the terms spoken in source audio correspond to the transcription output here.

| Term spoken in source audio | Abbreviation used in output | Example output |
| --- | --- | --- |
| Centigrade | C | The patient's temperature is 37.4 C. |
| Celsius | C | The patient's temperature is 37.4 C. |
| Fahrenheit | F | The patient's temperature is 101 F. |
| grams | g | A mass of 100 g was extracted from the patient. |
| meters | m | The patient is 1.8 m tall. |
| feet | ft | The patient is 6 ft tall. |
| kilos | kg | The patient weighs 80 kg. |
| kilograms | kg | The patient weighs 80 kg. |
| c c | cc | Patient received 100 cc of saline solution. |
| cubic centimeter | cc | Patient received 100 cc of saline solution. |
| milliliter | mL | Patient excreted 100 mL urine. |
| blood pressure | BP | Patient BP was elevated. |
| b p | BP | Patient BP was elevated. |
| X over Y | X/Y | Patient BP was 120/80. |
| beats per min | BPM | Patient had atrial fibrillation with heart rate of 160 BPM. |
| beats per minute | BPM | Patient had atrial fibrillation with heart rate of 160 BPM. |
| O 2 | O2 | Patient O2 saturation was 98%. |
| CO2 | CO2 | Patient required respiratory support for elevated CO2. |
| post operation | POSTOP | Patient came for POSTOP evaluation. |
| post op | POSTOP | Patient came for POSTOP evaluation. |
| cat scan | CT Scan | Patient indication of cerebral hemorrhage required use of CT Scan. |
| Pulse 80 | P 80 | Patient vitals were P 80, R 17,... |
| Respiration 17 | R 17 | Patient vitals were P 80, R 17,... |
| in and out | I/O | Patient was I/O sinus rhythm |
| L five | L5 | Lumbar puncture was performed between L4 and L5 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
