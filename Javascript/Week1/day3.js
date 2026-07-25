import dotenv from "dotenv";
import Groq from "groq-sdk";

dotenv.config({
    path: "../../.env",
});

const apiKey = process.env.GROQ_API_KEY;

if (!apiKey) {
    throw new Error("API key kaha hai bhai");
}

const client = new Groq({
    apiKey,
});

const model = "llama-3.3-70b-versatile";

const prompts = [
    "Hi!",
    "Explain time travel in Detail but under 100 words",
    "Write a 1000 word essay on Machine learning",
];

async function main() {
    for (const prompt of prompts) {
        const response = await client.chat.completions.create({
            model,
            messages: [
                {
                    role: "user",
                    content: prompt,
                },
            ],
            max_tokens: 5000,
        });

        const usage = response.usage;

        console.log(`
Prompt: ${prompt}
Prompt Tokens: ${usage.prompt_tokens}
Completion Tokens: ${usage.completion_tokens}
Total Tokens: ${usage.total_tokens}
Finish Reason: ${response.choices[0].finish_reason}
----------------------------------------
`);
    }
}

main().catch(console.error);
