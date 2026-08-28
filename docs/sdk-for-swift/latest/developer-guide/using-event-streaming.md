---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-event-streaming.html
---

# Event streaming with AWS SDK for Swift
<a name="using-event-streaming"></a>

## Overview
<a name="event-streaming-overview"></a>

Some AWS services provide timely feedback about the state of a system or process by streaming to your application a series of events describing that state, if your application wants to receive them. Likewise, other services may be able to receive a stream of events from your application to provide needed data as it becomes available. The AWS SDK for Swift provides support for sending and receiving streams of events with services that support this feature.

This section of the guide demonstrates how to stream events to a service and receive events from a service, with an example that uses Amazon Transcribe to transcribe voice content from an audio file into text displayed on the screen.

## Event streaming example
<a name="event-streaming-example"></a>

This Amazon Transcribe example uses the [swift-argument-parser](https://github.com/apple/swift-argument-parser) package from Apple to parse the command line neatly, as well as the `AWSTranscribeStreaming` module from the AWS SDK for Swift.

The example's complete source code is [available on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/transcribe-streaming/transcribe-events).

### Importing modules
<a name="event-streaming-example-imports"></a>

The example begins by importing the modules it needs:

```
import ArgumentParser
import AWSClientRuntime
import AWSTranscribeStreaming
import Foundation
```

### Enum definition
<a name="event-streaming-example-enum"></a>

Then an enum is defined to represent the three audio formats Amazon Transcribe supports for streaming. These are used to match against the format specified on the command line using the **--format** option.:

```
/// Identify one of the media file formats supported by Amazon Transcribe.
enum TranscribeFormat: String, ExpressibleByArgument {
    case ogg = "ogg"
    case pcm = "pcm"
    case flac = "flac"
}
```

### Creating the audio stream
<a name="event-streaming-example-createaudiostream"></a>

A function named `createAudioStream()` returns an `[AsyncThrowingStream](https://developer.apple.com/documentation/swift/asyncthrowingstream)` that contains the audio file's contents, broken into 125ms chunks. The `AsyncThrowingStream` supplies audio data to Amazon Transcribe. The stream is specified as an input property when calling the client's `[startStreamTranscription(input:)](https://sdk.amazonaws.com/swift/api/awstranscribestreaming/latest/documentation/awstranscribestreaming/transcribestreamingclient/startstreamtranscription(input:))` function.

```
    /// Create and return an Amazon Transcribe audio stream from the file
    /// specified in the arguments.
    ///
    /// - Throws: Errors from `TranscribeError`.
    ///
    /// - Returns: `AsyncThrowingStream<TranscribeStreamingClientTypes.AudioStream, Error>`
    func createAudioStream() async throws
                -> AsyncThrowingStream<TranscribeStreamingClientTypes.AudioStream, Error> {

        let fileURL: URL = URL(fileURLWithPath: path)
        let audioData = try Data(contentsOf: fileURL)

        // Properties defining the size of audio chunks and the total size of
        // the audio file in bytes. You should try to send chunks that last on
        // average 125 milliseconds.

        let chunkSizeInMilliseconds = 125.0
        let chunkSize = Int(chunkSizeInMilliseconds  / 1000.0 * Double(sampleRate) * 2.0)
        let audioDataSize = audioData.count

        // Create an audio stream from the source data. The stream's job is
        // to send the audio in chunks to Amazon Transcribe as
        // `AudioStream.audioevent` events.

        let audioStream = AsyncThrowingStream<TranscribeStreamingClientTypes.AudioStream,
                                Error> { continuation in
            Task {
                var currentStart = 0
                var currentEnd = min(chunkSize, audioDataSize - currentStart)

                // Generate and send chunks of audio data as `audioevent`
                // events until the entire file has been sent. Each event is
                // yielded to the SDK after being created.

                while currentStart < audioDataSize {
                    let dataChunk = audioData[currentStart ..< currentEnd]

                    let audioEvent = TranscribeStreamingClientTypes.AudioStream.audioevent(
                        .init(audioChunk: dataChunk)
                    )
                    let yieldResult = continuation.yield(audioEvent)
                    switch yieldResult {
                        case .enqueued(_):
                            // The chunk was successfully enqueued into the
                            // stream. The `remaining` parameter estimates how
                            // much room is left in the queue, but is ignored here.
                            break
                        case .dropped(_):
                            // The chunk was dropped because the queue buffer
                            // is full. This will cause transcription errors.
                            print("Warning: Dropped audio! The transcription will be incomplete.")
                        case .terminated:
                            print("Audio stream terminated.")
                            continuation.finish()
                            return
                        default:
                            print("Warning: Unrecognized response during audio streaming.")
                    }

                    currentStart = currentEnd
                    currentEnd = min(currentStart + chunkSize, audioDataSize)
                }

                // Let the SDK's continuation block know the stream is over.

                continuation.finish()
            }
        }

        return audioStream
    }
```

This function returns an `AsyncThrowingStream<[TranscribeStreamingClientTypes.AudioStream](https://sdk.amazonaws.com/swift/api/awstranscribestreaming/latest/documentation/awstranscribestreaming/transcribestreamingclienttypes/audiostream), Error>`. This is a function that asynchronously generates chunks of audio data, yielding them to the caller, until there's no audio left to process.

The function begins by creating a Foundation `URL` from the path of the audio file. Then it reads the audio into a `Data` object (to support larger audio files, this would need to be changed to load the audio from disk in chunks). The size of each audio chunk to send to the SDK is calculated so it will hold 125 milliseconds of audio, and the total size of the audio file in bytes is obtained.

The audio stream is generated by iterating over the audio data, taking the next chunk of audio and creating a `[TranscribeStreamingClientTypes.AudioStream.audioevent](https://sdk.amazonaws.com/swift/api/awstranscribestreaming/latest/documentation/awstranscribestreaming/transcribestreamingclienttypes/audioevent)` that represents it. The event is sent to the SDK using the continuation object's `yield()` function. The yield result is checked to see if any problems occurred, such as the event being dropped because the event queue is full.

This continues until the last chunk of audio is sent; then the continuation's `finish()` function is executed to let the SDK know the file has been fully transmitted.

### Transcribing audio
<a name="event-streaming-example-transcription"></a>

Transcription is handled by the `transcribe()` function:

```
    /// Run the transcription process.
    ///
    /// - Throws: An error from `TranscribeError`.
    func transcribe(encoding: TranscribeStreamingClientTypes.MediaEncoding) async throws {
        // Create the Transcribe Streaming client.

        let client = TranscribeStreamingClient(
            config: try await TranscribeStreamingClient.TranscribeStreamingClientConfiguration(
                region: region
            )
        )

        // Start the transcription running on the audio stream.

        let output = try await client.startStreamTranscription(
            input: StartStreamTranscriptionInput(
                audioStream: try await createAudioStream(),
                languageCode: TranscribeStreamingClientTypes.LanguageCode(rawValue: lang),
                mediaEncoding: encoding,
                mediaSampleRateHertz: sampleRate
            )
        )

        // Iterate over the events in the returned transcript result stream.
        // Each `transcriptevent` contains a list of result fragments which
        // need to be concatenated together to build the final transcript.
        for try await event in output.transcriptResultStream! {
            switch event {
            case .transcriptevent(let event):
            for result in event.transcript?.results ?? [] {
                guard let transcript = result.alternatives?.first?.transcript else {
                    continue
                }

                // If showing partial results is enabled and the result is
                // partial, show it. Partial results may be incomplete, and
                // may be inaccurate, with upcoming audio making the
                // transcription complete or by giving more context to make
                // transcription make more sense.

                if (result.isPartial && showPartial) {
                    print("[Partial] \(transcript)")
                }

                // When the complete fragment of transcribed text is ready,
                // print it. This could just as easily be used to draw the
                // text as a subtitle over a playing video, though timing
                // would need to be managed.

                if !result.isPartial {
                    if (showPartial) {
                        print("[Final  ] ", terminator: "")
                    }
                    print(transcript)
                }
            }
            default:
                print("Error: Unexpected message from Amazon Transcribe:")
            }
        }
    }
```

This function first looks at the value of the **--format** option passed into the program on the command line and prepares a constant of type `TranscribeStreamingClientTypes.MediaEncoding` that indicates the format of the incoming audio. Then it calls `[client.startStreamTranscription(input:)](https://sdk.amazonaws.com/swift/api/awstranscribestreaming/latest/documentation/awstranscribestreaming/transcribestreamingclient/startstreamtranscription(input:))` to start the transcription process. The audio stream is specified by a function named `createAudioStream()`, which is [described below](#event-streaming-example-createaudiostream).

The event stream returned by `startStreamTranscription(input:)` is monitored using a `for await` loop. Each `transcriptevent` is handled by pulling the first available transcription from the [result stream](https://sdk.amazonaws.com/swift/api/awstranscribestreaming/latest/documentation/awstranscribestreaming/transcribestreamingclienttypes/transcriptresultstream). If the transcript is flagged as partial and the user specified the **--show-partial** option on the command line, the partial output is printed to the console.

If it's a completed transcription of a section of the audio, the transcription is output to the screen. The importance of checking the value of the result's `isPartial` property is simple: as chunks of audio are processed, they may contain partial words that need to be completed by referring to other chunks. Similarly, if a transcription's certainty is low, it might be higher if subsequent chunks provide additional context. For example, if the transcription includes the word "its," the following chunk may help determine if the word should actually be "it's" instead.

### Running the example
<a name="event-streaming-example-running"></a>

If you download and build the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/transcribe-streaming/transcribe-events), you can run it using the **tsevents** executable. For example, if you have a 44,100Hz audio file named `audio-sample.flac`, you can process it with the command:

```
$ tsevents --path audio-sample.flac --format flac --sample-rate 44100
```

If the language of the audio file isn't US English, you can specify the file's language using the **--lang** option. For example, for modern Arabic, you can use:

```
$ tsevents --path audio-sample.flac --format flac --sample-rate 44100 --lang ar-SA
```

For complete usage information, simply run the command **tsevents --help**.

## Additional information
<a name="additional-information"></a>
+ [Amazon Transcribe Developer Guide](https://docs.aws.amazon.com/transcribe/latest/dg/)
+ [Amazon Transcribe API Reference](https://docs.aws.amazon.com/transcribe/latest/APIReference/Welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
