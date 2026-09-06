---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-action-fail.html
---

# Debugging unexpected ACTION\_FAILED events
<a name="unexpected-action-fail"></a>

If you receive an unexpected `ACTION_FAILED` event, check the following:

- **[CallAndBridge](call-and-bridge.md), [PlayAudio](play-audio.md), and [PlayAudioAndGetDigits](play-audio-get-digits.md)**
  - **Error Type:** InvalidAudioSource
  - **Error Message:** Cannot access S3 bucket or audio file.
  - **Resolution:**  +  Ensure the S3 bucket is in the same AWS account as the SIP media application. <br />+  Ensure the S3 bucket has given the `s3:GetObject` permissions to the `voiceconnector.chime.amazonaws.com` service principal.

- **[PlayAudio](play-audio.md), and [PlayAudioAndGetDigits](play-audio-get-digits.md)**
  - **Error Type:** InvalidAudioSource
  - **Error Message:** Audio Source parameter value is invalid.
  - **Resolution:**  +  Ensure you use a valid `Type`, such as S3. <br />+  Ensure that the S3 bucket grants the `s3:GetObject` permissions to the `voiceconnector.chime.amazonaws.com` service principal. <br />+  Ensure the `BucketName` field is not null or empty. <br />+  Ensure the `Key` field is not null or empty.

- **[CallAndBridge](call-and-bridge.md)**
  - **Error Type:** InvalidAudioSource / **Error Message:** Ringtone parameter value is invalid. / **Resolution:**  +  Ensure you use a valid `Type`, such as `S3`. <br />+  Ensure the `BucketName` field is not null or empty. <br />+  Ensure the `Key` field is not null or empty.
  - **Error Type:** InvalidActionParameter / **Error Message:** Invalid number of endpoints provided. / **Resolution:** Ensure the Endpoints are not null or zero and not greater than one.
  - **Error Type:** InvalidActionParameter / **Error Message:** Endpoint parameter is invalid. / **Resolution:**  +  Ensure Endpoint URI value is provided. <br />+  If the Endpoint Type is PSTN, make sure the phone number provided in the Uri field is a valid E.164 phone number. <br />+  If the Endpoint Type is PSTN, make sure that the ARN field is not set or is set to null.
  - **Error Type:** InvalidActionParameter / **Error Message:** Invalid caller ID. / **Resolution:** Provide a valid E.164 formatted phone number in the CallerId field.
  - **Error Type:** InvalidActionParameter / **Error Message:** Caller ID not defined. / **Resolution:** Provide a valid E.164 formatted phone number in the CallerId field.
  - **Error Type:** InvalidActionParameter / **Error Message:** The MaxCallTimeout parameter is invalid. Timeout must be between 0 and 120 seconds. / **Resolution:** Set the MaxCallTimeout interval to a value between 0 and 120 seconds.
  - **Error Type:** InvalidActionParameter / **Error Message:** Provided caller ID number is invalid. Number must be owned by this AWS account, or be the From number of LEG-A. / **Resolution:**  +  Ensure the `CallerId` number is provisioned and associated with the same AWS account as the SIP media application. <br />+  If the number is not associated with the account, it must match the number in the `From` field of LEG-A.
  - **Error Type:** InvalidActionParameter. / **Error Message:** Invalid SIP header(s) provided: {Header}. / **Resolution:**  +  Remove any internal custom headers: `x-vine`, `x-amzn`, `x-vc`, `x-canary`, `x-voice`. <br />+  Ensure your custom headers begin with `x-`. You can also set them to `user-to-user` or `diversion`.

- **[JoinChimeMeeting](join-chime-meeting.md)**
  - **Error Type:** InvalidActionParameter.
  - **Error Message:** JoinToken parameter value is invalid.
  - **Resolution:**  +  Verify that the meeting join token is correct. <br />+  Verify that the participant that the token is associated with is still a valid attendee of the meeting. <br />+  Verify that the meeting still exists.

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
  - **Error Type:** InvalidActionParameter / **Error Message:** The RecordingDestination parameter is invalid. / **Resolution:**  +  Verify that the `Type` field is valid, such as S3. <br />+  Verify that the `BucketName` field is not empty or null. <br />+  Verify that the prefix consists of valid characters. <br />+  Verify that the prefix is less than or equal to 979 bytes.
  - **Error Type:** InvalidActionParameter / **Error Message:** The DurationInSeconds parameter is invalid. / **Resolution:** DurationInSeconds must not be null and must be greater than 0.
  - **Error Type:** InvalidActionParameter / **Error Message:** The SilenceThreshold parameter is invalid. / **Resolution:** SilenceThreshold must not be null and must be between 1 and 1000.
  - **Error Type:** InvalidActionParameter / **Error Message:** The SilenceDurationInSeconds parameter is invalid. / **Resolution:** SilenceDurationInSeconds must not be null and must be greater than 0.
  - **Error Type:** InvalidActionParameter / **Error Message:** An error occurred while uploading the recording to the S3 bucket. / **Resolution:**  +  Ensure the S3 bucket is in the same AWS account as the SIP media application. <br />+  Ensure that the S3 bucket has granted `s:PutObject` and s`:PutObjectAcl` permissions to use to the `voiceconnector.chime.amazonaws.com` service principal.

- **[Understanding VoiceFocus for the Amazon Chime SDK PTSN audio service](voice-focus.md)**
  - **Error Type:** MissingRequiredActionParameter
  - **Error Message:** Missing a required action parameter.
  - **Resolution:** Provide a valid boolean value for the Enable parameter.
