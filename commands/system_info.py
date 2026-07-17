import psutil
import platform


def sistem():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    return (
        f"CPU kullanımı: %{cpu}\n"
        f"RAM kullanımı: %{ram}\n"
        f"Sistem: {platform.system()}"
    )
