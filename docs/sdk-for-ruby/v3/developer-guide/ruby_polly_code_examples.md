---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/ruby_polly_code_examples.html
---

# Amazon Polly examples using SDK for Ruby
<a name="ruby_polly_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Ruby with Amazon Polly.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Actions
<a name="actions"></a>

### `DescribeVoices`
<a name="polly_DescribeVoices_ruby_topic"></a>

The following code example shows how to use `DescribeVoices`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/polly#code-examples).

```
require 'aws-sdk-polly' # In v2: require 'aws-sdk'

begin
  # Create an Amazon Polly client using
  # credentials from the shared credentials file ~/.aws/credentials
  # and the configuration (region) from the shared configuration file ~/.aws/config
  polly = Aws::Polly::Client.new

  # Get US English voices
  resp = polly.describe_voices(language_code: 'en-US')

  resp.voices.each do |v|
    puts v.name
    puts "  #{v.gender}"
    puts
  end
rescue StandardError => e
  puts 'Could not get voices'
  puts 'Error message:'
  puts e.message
end
```
+  For API details, see [DescribeVoices](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/DescribeVoices) in *AWS SDK for Ruby API Reference*.

### `ListLexicons`
<a name="polly_ListLexicons_ruby_topic"></a>

The following code example shows how to use `ListLexicons`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/polly#code-examples).

```
require 'aws-sdk-polly' # In v2: require 'aws-sdk'

begin
  # Create an Amazon Polly client using
  # credentials from the shared credentials file ~/.aws/credentials
  # and the configuration (region) from the shared configuration file ~/.aws/config
  polly = Aws::Polly::Client.new

  resp = polly.list_lexicons

  resp.lexicons.each do |l|
    puts l.name
    puts "  Alphabet:#{l.attributes.alphabet}"
    puts "  Language:#{l.attributes.language}"
    puts
  end
rescue StandardError => e
  puts 'Could not get lexicons'
  puts 'Error message:'
  puts e.message
end
```
+  For API details, see [ListLexicons](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/ListLexicons) in *AWS SDK for Ruby API Reference*.

### `SynthesizeSpeech`
<a name="polly_SynthesizeSpeech_ruby_topic"></a>

The following code example shows how to use `SynthesizeSpeech`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/polly#code-examples).

```
require 'aws-sdk-polly' # In v2: require 'aws-sdk'

begin
  # Get the filename from the command line
  if ARGV.empty?
    puts 'You must supply a filename'
    exit 1
  end

  filename = ARGV[0]

  # Open file and get the contents as a string
  if File.exist?(filename)
    contents = IO.read(filename)
  else
    puts "No such file: #{filename}"
    exit 1
  end

  # Create an Amazon Polly client using
  # credentials from the shared credentials file ~/.aws/credentials
  # and the configuration (region) from the shared configuration file ~/.aws/config
  polly = Aws::Polly::Client.new

  resp = polly.synthesize_speech({
                                   output_format: 'mp3',
                                   text: contents,
                                   voice_id: 'Joanna'
                                 })

  # Save output
  # Get just the file name
  #  abc/xyz.txt -> xyx.txt
  name = File.basename(filename)

  # Split up name so we get just the xyz part
  parts = name.split('.')
  first_part = parts[0]
  mp3_file = "#{first_part}.mp3"

  IO.copy_stream(resp.audio_stream, mp3_file)

  puts "Wrote MP3 content to: #{mp3_file}"
rescue StandardError => e
  puts 'Got error:'
  puts 'Error message:'
  puts e.message
end
```
+  For API details, see [SynthesizeSpeech](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/SynthesizeSpeech) in *AWS SDK for Ruby API Reference*.

## Scenarios
<a name="scenarios"></a>

### Create an application to analyze customer feedback
<a name="cross_FSA_ruby_topic"></a>

The following code example shows how to create an application that analyzes customer comment cards, translates them from their original language, determines their sentiment, and generates an audio file from the translated text.

**SDK for Ruby**
 This example application analyzes and stores customer feedback cards. Specifically, it fulfills the need of a fictitious hotel in New York City. The hotel receives feedback from guests in various languages in the form of physical comment cards. That feedback is uploaded into the app through a web client. After an image of a comment card is uploaded, the following steps occur:
+ Text is extracted from the image using Amazon Textract.
+ Amazon Comprehend determines the sentiment of the extracted text and its language.
+ The extracted text is translated to English using Amazon Translate.
+ Amazon Polly synthesizes an audio file from the extracted text.
 The full app can be deployed with the AWS CDK. For source code and deployment instructions, see the project in [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/cross_service_examples/feedback_sentiment_analyzer).

**Services used in this example**
+ Amazon Comprehend
+ Lambda
+ Amazon Polly
+ Amazon Textract
+ Amazon Translate
