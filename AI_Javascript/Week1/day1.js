import dotenv from "dotenv";
import Groq from "groq-sdk/index.js";

dotenv.config({
    path: "../../.env"
});

// Read API Key
const myApiKey = process.env.GROQ_API_KEY;

if (!myApiKey) {
    throw new Error("Where is API key");
}

// Create Client
const client = new Groq({
    apiKey: myApiKey,
});

// Variables
const model = "llama-3.3-70b-versatile";
const role = "user";
const prompt = "What is Server Side Rendering";

// Message Object
const message = {
    role,
    content: prompt,
};

const messages = [message];

async function main() {
    try {
        const response = await client.chat.completions.create({
            model,
            messages,
        });

        // console.log(response);

        console.log("#######################################");

        const answer = response.choices[0].message.content;

        console.log(answer);
    } catch (error) {
        console.error(error);
    }
}

main();