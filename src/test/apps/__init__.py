from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Columns,
    FilterMenu,
    FilterMenus,
    RowActionNorth,
    RowActions,
    Rows,
)

schema_name = 'nomad_hysprint.schema_packages.hysprint_package.HySprint_VoilaNotebook'

app_entry_point = AppEntryPoint(
    name='NewApp',
    description='New app entry point configuration.',
    app=App(
        label='NewApp',
        path='app',
        category='simulation',
        columns=Columns(
            selected=['entry_id'],
            options={
                'entry_id': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
            }
        ),
        rows=Rows(
            actions=RowActions(
                options={
                    'launch': RowActionNorth(
                        tool_name='voila',
                        filepath=f'data.notebook_file#{schema_name}',
                    )
                }
            ),
        ),
    ),
)
