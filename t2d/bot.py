from discord import Message
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands.view import StringView
from loguru import logger
import typer

from t2d.utils import run_app_command, get_version


class T2D(commands.Bot):
    def __init__(
        self,
        cli_app: typer.Typer,
        command_prefix: str = "!",
        ignore_bots: bool = True,
        *args,
        **kwargs
    ):
        super().__init__(
            command_prefix=command_prefix,
            *args,
            **kwargs
        )

        self.app = cli_app
        self.ignore_bots = ignore_bots
        self.logger = logger

        @self.command(
            name="t2d",
            help="Runs Typer CLI app using T2D"
        )
        async def t2d(ctx: Context):
            view = StringView(ctx.message.content)
            view.skip_string(ctx.prefix)
            view.skip_string("t2d")
            view.skip_string(" ")
            args = view.read_rest().split(" ")
            if len(args) == 1 and args[0] == "":
                args = []
            stdout, stderr = run_app_command(self.app, args)
            if len(stdout) > 0 and len(stderr) > 0:
                await ctx.send(f"```{stdout}\n{stderr}```")
            elif len(stdout) > 0:
                await ctx.send(f"```{stdout}```")
            elif len(stderr) > 0:
                await ctx.send(f"```{stderr}```")

        @self.command(
            name="version",
            help="Prints T2D version"
        )
        async def version(ctx: Context):
            await ctx.send(f"T2D version: {get_version()}")

    async def on_ready(self):
        self.logger.info("Bot is ready!")
        self.logger.info(f"Logged in as {self.user.name}")

    async def on_command_error(self, ctx, error):
        self.logger.error(error)
