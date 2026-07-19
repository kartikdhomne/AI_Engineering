import dotenv from "dotenv";
import Groq from "groq-sdk";

dotenv.config({
    path: "../../../.env",
});

const my_api_key = process.env.GROQ_API_KEY;

if (!my_api_key) {
    throw new Error("API key kaha hai bhai");
}

const client = new Groq({
    apiKey: my_api_key,
});

const model = "llama-3.3-70b-versatile";
const role = "user";
const prompt = "Suggest a name for my cloth company brand";

// message me role and content
const message_system = {
    role: "system",
    content:
        "You are a brand manager who suggests name for my food brand, name should be in one word, suggest one name only",
};

const message = {
    role: role,
    content: prompt,
};

const messages = [message_system, message];

async function main() {
    try {
        const response = await client.chat.completions.create({
            model: model,
            messages: messages,
            temperature: 0,
        });

        console.log(response);

        console.log("#######################################");

        const answer = response.choices[0].message.content;
        console.log(answer);
    } catch (error) {
        console.error(error);
    }
}

main();
