# t2d

`t2d` is a short for Typer-to-Discord. It implements a seamless integration between Typer and Discord.py for CLI Discord bots development.

## Installing

Just install the package using `pip install t2d`.

## How to use it?

Assume that you have a Typer app that looks something like this:

```py
import typer
app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}!")

@app.command()
def bye(name: str):
    typer.echo(f"Bye {name}!")
```

All you have to do is:

```py
import t2d
bot = t2d.T2D(app)
bot.run(YOUR_DISCORD_BOT_TOKEN)
```

And that's it! Now you can use your Typer app in Discord! Default commands are:

```
!help    Shows default help message for the bot
!t2d     Runs Typer CLI app using T2D
!version Prints T2D version
```

Following with the example above, you can do the following:

```
!t2d hello Gabriel -> Shows "Hello Gabriel!"
!t2d bye Gabriel   -> Shows "Bye Gabriel!"
```

## Extending T2D

One can also extend T2D as it normally would using the `discord.ext.commands.Bot` API.
