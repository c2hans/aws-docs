---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html
---

# Debugging unexpected ACTION\_FAILED events
<a name="unexpected-action-fail"></a>

If you receive an unexpected `ACTION_FAILED` event, check the following:

- **[CallAndBridge](call-and-bridge.md), [PlayAudio](play-audio.md), and [PlayAudioAndGetDigits](play-audio-get-digits.md)**
  - **Error Type:** InvalidAudioSource
  - **Error Message:** Cannot access S3 bucket or audio file.
  - **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)

- **[PlayAudio](play-audio.md), and [PlayAudioAndGetDigits](play-audio-get-digits.md)**
  - **Error Type:** InvalidAudioSource
  - **Error Message:** Audio Source parameter value is invalid.
  - **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)

- **[CallAndBridge](call-and-bridge.md)**
  - **Error Type:** InvalidAudioSource / **Error Message:** Ringtone parameter value is invalid. / **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)
  - **Error Type:** InvalidActionParameter / **Error Message:** Invalid number of endpoints provided. / **Resolution:** Ensure the Endpoints are not null or zero and not greater than one.
  - **Error Type:** InvalidActionParameter / **Error Message:** Endpoint parameter is invalid. / **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)
  - **Error Type:** InvalidActionParameter / **Error Message:** Invalid caller ID. / **Resolution:** Provide a valid E.164 formatted phone number in the CallerId field.
  - **Error Type:** InvalidActionParameter / **Error Message:** Caller ID not defined. / **Resolution:** Provide a valid E.164 formatted phone number in the CallerId field.
  - **Error Type:** InvalidActionParameter / **Error Message:** The MaxCallTimeout parameter is invalid. Timeout must be between 0 and 120 seconds. / **Resolution:** Set the MaxCallTimeout interval to a value between 0 and 120 seconds.
  - **Error Type:** InvalidActionParameter / **Error Message:** Provided caller ID number is invalid. Number must be owned by this AWS account, or be the From number of LEG-A. / **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)
  - **Error Type:** InvalidActionParameter. / **Error Message:** Invalid SIP header(s) provided: {Header}. / **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)

- **[JoinChimeMeeting](join-chime-meeting.md)**
  - **Error Type:** InvalidActionParameter.
  - **Error Message:** JoinToken parameter value is invalid.
  - **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)

- ** [ModifyChimeMeetingAttendee (muting and unmuting audio)](mute-unmute.md) **
  - **Error Type:** InvalidActionParameter / **Error Message:** The value in the Operation field of the ModifyChimeMeetingAttendees action is invalid. / **Resolution:** Ensure that the service supports muting and unmuting operations.
  - **Error Type:** InvalidActionParameter / **Error Message:** The meeting ID parameter is invalid. / **Resolution:** Ensure the meeting ID is correct.
  - **Error Type:** InvalidActionParameter / **Error Message:** Attendee List parameter is invalid. / **Resolution:** You provided no attendees, or you provided more than 100 attendees. Provide between 1 and 100 attendees.
  - **Error Type:** InvalidActionParameter / **Error Message:** One or more attendees are not part of this meeting. All attendees must be part of this meeting. / **Resolution:** One of the attendees provided in the action is not a valid participant of the meeting specified. Remove any attendee not in the meeting.

- **[Pause](pause.md)**
  - **Error Type:** InvalidActionParameter
  - **Error Message:** The Duration parameter is invalid.
  - **Resolution:** Set the pause duration to between 100 and 30000.

- **[PlayAudioAndGetDigits](play-audio-get-digits.md)**
  - **Error Type:** InvalidActionParameter / **Error Message:** The MaxNumberOfDigits parameter is invalid. / **Resolution:** Ensure MaxNumberOfDigits is between 0 and 128, and that it's greater than MinNumberOfDigits/
  - **Error Type:** InvalidActionParameter / **Error Message:** The RepeatDurationInMilliseconds parameter is invalid. / **Resolution:** Ensure the RepeatDurationInMilliseconds value is positive.
  - **Error Type:** InvalidActionParameter / **Error Message:** The InputDigitsRegex parameter is invalid. / **Resolution:** Ensure the InputDigitsRegex is a valid regex pattern.

- **[ReceiveDigits](listen-to-digits.md)**
  - **Error Type:** InvalidActionParameter / **Error Message:** The InBetweenDigitsDurationInMilliseconds parameter is invalid. / **Resolution:** Ensure the value is greater than 0.
  - **Error Type:** InvalidActionParameter / **Error Message:** The FlushDigitsDurationInMilliseconds parameter is invalid. / **Resolution:** The FlushDigitsDurationInMilliseconds interval is less than or equal to the InBetweenDigitsDurationInMilliseconds interval. Make the InBetweenDigitsDurationInMilliseconds interval greater than the FlushDigitsDurationInMilliseconds interval.
  - **Error Type:** InvalidActionParameter / **Error Message:** The InputDigitsRegex parameter is invalid. / **Resolution:** Ensure the value is not empty or null.

- ** [RecordAudio](record-audio.md) **
  - **Error Type:** InvalidActionParameter / **Error Message:** The RecordingDestination parameter is invalid. / **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)
  - **Error Type:** InvalidActionParameter / **Error Message:** The DurationInSeconds parameter is invalid. / **Resolution:** DurationInSeconds must not be null and must be greater than 0.
  - **Error Type:** InvalidActionParameter / **Error Message:** The SilenceThreshold parameter is invalid. / **Resolution:** SilenceThreshold must not be null and must be between 1 and 1000.
  - **Error Type:** InvalidActionParameter / **Error Message:** The SilenceDurationInSeconds parameter is invalid. / **Resolution:** SilenceDurationInSeconds must not be null and must be greater than 0.
  - **Error Type:** InvalidActionParameter / **Error Message:** An error occurred while uploading the recording to the S3 bucket. / **Resolution:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html)

- **[Understanding VoiceFocus for the Amazon Chime SDK PTSN audio service](voice-focus.md)**
  - **Error Type:** MissingRequiredActionParameter
  - **Error Message:** Missing a required action parameter.
  - **Resolution:** Provide a valid boolean value for the Enable parameter.
