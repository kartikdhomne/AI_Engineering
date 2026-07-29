import dotenv from "dotenv";
import Groq from "groq-sdk";

dotenv.config({
    path: "../../.env"
});

const apiKey = process.env.GROQ_API_KEY;

if (!apiKey) {
    throw new Error("API key kaha hai bhai");
}

const client = new Groq({
    apiKey,
});

const model = "llama-3.3-70b-versatile";

async function llmAns(prompt) {
    const messages = [
        {
            role: "user",
            content: prompt,
        },
    ];

    const response = await client.chat.completions.create({
        model,
        messages,
    });

    return response.choices[0].message.content;
}

const badPrompt = `
#ROLE:
You are a support assistant at a mobile/laptop company.

#TASK
You have to classify the issue into a category.

#CONSTRAINT
You have to classify the issue into one of three categories:
- Billing
- Technical
- Return

#OUTPUT FORMAT
Your answer should be only one word.
The word must be one of:
Billing
Technical
Return

#EXAMPLE
If a user asks for a refund, the category is Return.

#FALLBACK
If the complaint doesn't match any category, return:
OTHER

User Complaint:
I want refund
`;

async function main() {
    try {
        const answer = await llmAns(badPrompt);
        console.log(answer);
    } catch (error) {
        console.error(error);
    }
}

main();