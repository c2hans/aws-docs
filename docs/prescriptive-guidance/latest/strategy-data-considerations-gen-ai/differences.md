---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/differences.html
---

# Data differences between generative AI and traditional ML
<a name="differences"></a>

The landscape of artificial intelligence is marked by a fundamental distinction between traditional machine learning approaches and modern generative AI systems, particularly in how they process and utilize data. This comprehensive analysis explores three key dimensions of this technological evolution: the structural differences between data types, their processing requirements, and the diverse modalities of data that modern AI systems can handle. It also highlights how synthetic data that is created by generative AI is emerging as a new source of training data. Synthetic data makes it possible to implement traditional ML use cases that were previously limited by data scarcity and data privacy constraints. Understanding these distinctions is crucial for organizations because it helps you navigate the complexities of data management, model training, and practical applications across various industries.

**This section contains the following topics:**
+ [Structured and unstructured data](#differences-structure)
+ [Diverse data modalities](#differences-modalities)
+ [Data synthesizing for traditional ML](#differences-synthesizing)

## Structured and unstructured data
<a name="differences-structure"></a>

Traditional ML models and modern generative AI systems diverge significantly in their data requirements and the nature of the data that they handle.

Traditional ML uses data that is organized in tables or fixed schemas or curated image and audio datasets that have annotations. Examples include predictive models that analyze tabular data or classic computer vision. These systems often rely on structured, labeled datasets. For supervised learning, each data point usually comes with an explicit label or target, such as an image labeled `cat` or a row of sales data that has a target value.

By contrast, generative AI models thrive on unstructured** **or semi-structured** **data. This includes large language models (LLMs) and generative vision or audio models. They do not require explicit labels for pre-training, which is when they learn general language understanding from a massive, diverse dataset. This distinction is key—generative models can ingest and learn from vast amounts of text or images without manual labeling. This is something that traditional, supervised ML cannot do.

To excel at specific tasks or domains, these pre-trained LLMs require *task-specific training*, which is often called *fine-tuning*. It involves further training the pre-trained model on a smaller, specialized dataset with instructions or completion pairs. In this way, fine-tuning a generative AI model is like the process of supervised training for a traditional ML model.

## Diverse data modalities
<a name="differences-modalities"></a>

Modern generative AI models process and produce a wide range of data types: text, code, images, audio, video, and even combinations, known as *multimodal data*. For example, foundation models such as Anthropic Claude, are trained on textual data (web pages, books, articles) and even large repositories of code. Generative vision models, such as Amazon Nova Canvas or Stable Diffusion, learn from images that are often paired with text (captions or labels). Generative audio models might consume sound wave data or transcripts to generate speech or music.

Generative AI systems are increasingly multimodal. These systems can process and produce combinations of text, images, audio, with an ability to handle unstructured text and media at scale. They can learn the nuances of language, vision, and sound that traditional structured-data ML cannot. This flexibility contrasts with typical ML models, which usually specialize in one data type at a time. For example, an image classifier model can't generate text, or a natural language processing (NLP) model that is trained for sentiment analysis can't create images.

Even LLMs have limits. When it comes to processing tabular data, such as CSV files, LLMs face notable challenges during inference. The [Uncovering Limitations of Large Language Models in Information Seeking from Tables](https://arxiv.org/abs/2406.04113) study highlights that LLMs often struggle with understanding table structures and accurately extracting information. The research found that the models' performance ranged from marginally satisfactory to inadequate, revealing a poor grasp of table structures. The inherent design of LLMs contributes to these limitations. They are primarily trained on sequential text data, which equips them to predict and generate text-based content. However, this training does not translate seamlessly to interpreting tabular data, where understanding the relationships between rows and columns is crucial. As a result, LLMs can misinterpret the context or significance of numerical data within tables, leading to inaccurate analyses.

In essence, an enterprise data strategy for generative AI must account for far more unstructured content than before. Organizations need to evaluate their body of text (documents, emails, knowledge bases), code repositories, audio and video archives, and other unstructured data sources – not just the neatly organized tables in their data warehouse.

## Data synthesizing for traditional ML
<a name="differences-synthesizing"></a>

Generative AI can overcome some longstanding barriers faced by traditional machine learning, particularly those related to data scarcity and privacy constraints. By using foundation models to generate *synthetic data*—artificial datasets that closely mimic real-world distributions—organizations can now unlock ML use cases that were previously out of reach due to data scarcity, privacy concerns, and the high costs associated with collecting and annotating large datasets.

In healthcare, for instance, synthetic medical images have been used to augment existing datasets. This can enhance diagnostic models while safeguarding patient confidentiality. In the financial sector, synthetic data can help you simulate market scenarios, which aids with risk assessment and algorithmic trading without exposing sensitive information.  Synthetic data that simulates diverse driving conditions benefits autonomous vehicle development. It facilitates the training of computer vision systems in scenarios that are challenging to capture in real life. By using foundation models for synthetic data generation, organizations can enhance ML model performance, comply with data privacy regulations, and unlock new use cases across various industries.
