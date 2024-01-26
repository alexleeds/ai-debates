import os
import anthropic_bedrock
from anthropic_bedrock import AnthropicBedrock

# Access environment variables
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token = os.getenv('AWS_SESSION_TOKEN', None)  # Default to None if not set
aws_region = os.getenv('AWS_REGION', 'us-east-2')  # Default to 'us-east-2' if not set

client = AnthropicBedrock(
    # Authenticate using the environment variables
    aws_access_key=aws_access_key,
    aws_secret_key=aws_secret_key,
    # Temporary credentials can be used with aws_session_token.
    aws_session_token=aws_session_token,
    # aws_region changes the aws region to which the request is made.
    aws_region=aws_region,
)

completion = client.completions.create(
    model="amazon.titan-tg1-large",
    max_tokens_to_sample=256,
    prompt=f"{anthropic_bedrock.HUMAN_PROMPT} Tell me a funny joke about outer space! {anthropic_bedrock.AI_PROMPT}",
)
print(completion.completion)
