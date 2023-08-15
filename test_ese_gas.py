import main
from mockito import when
import pandas as pd


def test_success_crew_presence_gt_30_min_and_lt_60_min():
    en_data = {'gas reading time': ['2021-12-06T12:00:00.000Z'], 'entry time': ['2021-12-06T12:00:00.000Z'],
               'exit time': ['2021-12-06T12:50:00.000Z']}
    pd_data = {'gas reading time': ['2021-12-06T11:00:00.000Z', '2021-12-06T11:30:00.000Z', '2021-12-06T12:30:00.000Z']}
    ref = main
    when(ref).read_input_files().thenReturn([pd.DataFrame(en_data), pd.DataFrame(pd_data)])
    assert main.check_gas_testing_time_compliance()


def test_failure_crew_presence_gt_30_min_and_lt_60_min():
    en_data = {'gas reading time': ['2021-12-06T12:00:00.000Z'], 'entry time': ['2021-12-06T12:00:00.000Z'],
               'exit time': ['2021-12-06T12:50:00.000Z']}
    pd_data = {'gas reading time': ['2021-12-06T11:00:00.000Z', '2021-12-06T11:30:00.000Z', '2021-12-06T13:00:00.000Z']}
    ref = main
    when(ref).read_input_files().thenReturn([pd.DataFrame(en_data), pd.DataFrame(pd_data)])
    assert not main.check_gas_testing_time_compliance()


def test_success_crew_presence_gt_60_minutes():
    en_data = {'gas reading time': ['2021-12-06T12:00:00.000Z'], 'entry time': ['2021-12-06T12:00:00.000Z'],
               'exit time': ['2021-12-06T13:50:00.000Z']}
    pd_data = {'gas reading time': ['2021-12-06T11:00:00.000Z', '2021-12-06T11:30:00.000Z', '2021-12-06T12:30:00.000Z',
                                    '2021-12-06T13:00:00.000Z', '2021-12-06T13:30:00.000Z']}
    ref = main
    when(ref).read_input_files().thenReturn([pd.DataFrame(en_data), pd.DataFrame(pd_data)])
    assert main.check_gas_testing_time_compliance()


def test_failure_crew_presence_gt_60_minutes():
    en_data = {'gas reading time': ['2021-12-06T12:00:00.000Z'], 'entry time': ['2021-12-06T12:00:00.000Z'],
               'exit time': ['2021-12-06T13:50:00.000Z']}
    pd_data = {'gas reading time': ['2021-12-06T11:00:00.000Z', '2021-12-06T11:30:00.000Z', '2021-12-06T12:30:00.000Z',
                                    '2021-12-06T13:00:00.000Z', '2021-12-06T13:31:00.000Z']}
    ref = main
    when(ref).read_input_files().thenReturn([pd.DataFrame(en_data), pd.DataFrame(pd_data)])
    assert not main.check_gas_testing_time_compliance()


def test_success_crew_presence_lt_30_minutes():
    en_data = {'gas reading time': ['2021-12-06T12:00:00.000Z'], 'entry time': ['2021-12-06T12:00:00.000Z'],
               'exit time': ['2021-12-06T12:25:00.000Z']}
    pd_data = {'gas reading time': ['2021-12-06T11:00:00.000Z', '2021-12-06T11:30:00.000Z', '2021-12-06T12:30:00.000Z']}
    ref = main
    when(ref).read_input_files().thenReturn([pd.DataFrame(en_data), pd.DataFrame(pd_data)])
    assert main.check_gas_testing_time_compliance()


def test_success_invalid_input_data():
    en_data = {'gas reading time': [], 'entry time': [], 'exit time': []}
    pd_data = {'gas reading time': ['2021-12-06T11:00:00.000Z', '2021-12-06T11:30:00.000Z', '2021-12-06T12:30:00.000Z']}
    ref = main
    when(ref).read_input_files().thenReturn([pd.DataFrame(en_data), pd.DataFrame(pd_data)])
    assert main.check_gas_testing_time_compliance()
