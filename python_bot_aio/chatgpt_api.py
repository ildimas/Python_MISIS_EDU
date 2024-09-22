from openai import OpenAI
import os
import time
import logging



#! Actual meaning part
class ChatGPT_asistant_creator:
    def __init__(self):
        client = OpenAI(
        api_key="апи ключ",
        organization="орагнизация "
        )
        model = "gpt-4o"
        #! ==  Create our Assistant (Uncomment this to create your assistant) ==
        assis = client.beta.assistants.create(
            name="Answer bot",
            instructions="""You are base chat-gpt""",
            model=model,
        )
        asistant_id = assis.id
        print(asistant_id)
        #! ==  Create our Assistant (Uncomment this to create your assistant) ==

        #! === Thread (uncomment this to create your Thread) ===
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": "Приступим к работе !",
                }
            ]
        )
        thread_id = thread.id
        print(thread_id)
        #! === Thread (uncomment this to create your Thread) ===



class ChatGPT_acsess_point:
    def __init__(self, user_prompt):
        self.user_prompt = user_prompt
        self.client = OpenAI(
        organization="организация ",
        api_key="апи ключ",
        )
        self.assistant_id="id асистента"
        
        self.thread = self.client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": "Приступим к работе !",
                }
            ]
        )
        self.content = self.user_prompt
        self.request = self.client.beta.threads.messages.create(thread_id=self.thread.id, role="user", content=self.content)
        self.run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id
        )
        print(self.request.assistant_id, self.request.thread_id)

    async def wait_for_run_completion(self, sleep_interval=3):
        """

        Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
        :param thread_id: The ID of the thread.
        :param run_id: The ID of the run.
        :param sleep_interval: Time in seconds to wait between checks.
        """
        while True:
            try:
                run = self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=self.run.id)
                if run.completed_at:
                    elapsed_time = run.completed_at - run.created_at
                    formatted_elapsed_time = time.strftime(
                        "%H:%M:%S", time.gmtime(elapsed_time)
                    )
                    print(f"Run completed in {formatted_elapsed_time}")
                    logging.info(f"Run completed in {formatted_elapsed_time}")
                    # Get messages here once Run is completed!
                    messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
                    last_message = messages.data[0]
                    response = last_message.content[0].text.value
                    print(f"Assistant Response: {response}")
                    return response
            except Exception as e:
                print("ERROR: ", e)
                logging.error(f"An error occurred while retrieving the run: {e}")
                break
            
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)

# === Run ===
if __name__ == "__main__":
    x = ChatGPT_acsess_point("Айоу мистер вайт - откуда фраза ?")
    x.wait_for_run_completion()
    # y = ChatGPT_asistant_creator()