
## reservation 1
* make_reservation
  - utter_choose_time
* give_time
  - utter_time_confirm
* confirm_time
  - utter_success
* bye

## reservation 2
* make_reservation
  - utter_choose_time
* give_time_number
  - action_time_number_confirm
* confirm_time
  - utter_success
* bye

## wait for consulting
* wait_consult
  - utter_please_wait
