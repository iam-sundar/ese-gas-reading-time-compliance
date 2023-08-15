import pandas as pd


def read_input_files():
    en_df = pd.read_csv('entrant_gas_reading.csv')
    pd_df = pd.read_csv('periodical_gas_reading.csv')
    return en_df, pd_df


def check_gas_testing_time_compliance() -> bool:
    compliance_flag = True
    en_df, pd_df = read_input_files()
    pd_df['gas reading time ts'] = pd.to_datetime(pd_df['gas reading time'])

    ''' Assumption: As per main.py file skeleton, the entrant file contain only one entry and do 
        compliance status validation of it. '''

    if len(en_df) == 1:
        reading_gap = 30

        '''Getting value from Entrant file and conversion from STRING to Timestamp'''
        entry_ts = pd.Timestamp(en_df['entry time'][0])
        exit_ts = pd.Timestamp(en_df['exit time'][0])

        ''' Finding crew member presence duration inside the enclosed space. '''
        crew_duration = (exit_ts - entry_ts) / pd.Timedelta(minutes=1)

        ''' Check: Crew member present inside the enclosed space for more than 30 min. '''
        if crew_duration > reading_gap:

            ''' It implies crew member present inside the enclosed space for more than 30 min. 
            So there will be a entry in periodical gas reading at end of every 30 min. '''
            no_of_reading_expected = int(crew_duration // reading_gap)

            ''' Calculating possible reading time.'''
            for i in range(no_of_reading_expected):
                possible_reading_ts = (entry_ts + pd.Timedelta(minutes=(i + 1) * reading_gap)).to_datetime64()
                presence = False
                ''' As per problem statement, eligible reading time starts from 25 min to 30 min. '''
                for j in range(6):
                    if possible_reading_ts in pd_df['gas reading time ts'].values:
                        presence = True
                        break
                    else:
                        possible_reading_ts = (possible_reading_ts + pd.Timedelta(minutes=-1)).to_datetime64()

                if not presence:
                    compliance_flag = False
                    break
        else:
            print('No validation required.')
    else:
        ''' Assumption: As per main.py file skeleton, the entrant file contain only one entry and do 
        compliance status validation of it. '''
        print('Invalid input.')
    return compliance_flag


if __name__ == "__main__":
    if check_gas_testing_time_compliance():
        print("Compliant")
    else:
        print("Not Compliant")
